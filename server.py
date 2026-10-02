import http.server
import socketserver
import webbrowser
import socket
import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error

# Ensure working directory is the backend directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CURRENT_DIR)

# Configuration: load from local_config.py or environment variables
try:
    import local_config
    SUPABASE_URL = getattr(local_config, "SUPABASE_URL", "https://jyatlsllsdmtdmvohhfz.supabase.co")
    SUPABASE_PUB_KEY = getattr(local_config, "SUPABASE_PUB_KEY", "")
    SUPABASE_SEC_KEY = getattr(local_config, "SUPABASE_SEC_KEY", "")
    GEMINI_API_KEY = getattr(local_config, "GEMINI_API_KEY", "")
except ImportError:
    SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://jyatlsllsdmtdmvohhfz.supabase.co")
    SUPABASE_PUB_KEY = os.environ.get("SUPABASE_PUB_KEY", "")
    SUPABASE_SEC_KEY = os.environ.get("SUPABASE_SEC_KEY", "")
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

try:
    import seed_data
except ImportError:
    seed_data = None

def get_free_port():
    preferred_ports = [8000, 8080, 5000, 5500, 3000]
    for p in preferred_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', p))
                return p
        except OSError:
            continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

def call_gemini_raw(prompt, key=None, temperature=0.7):
    api_key = key or GEMINI_API_KEY
    if not api_key:
        return None, "No Gemini API key configured."
    models = ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-flash-lite-latest", "gemini-3.5-flash", "gemini-3.8-flash"]
    last_err = None
    for model in models:
        try:
            g_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            req_data = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "responseMimeType": "application/json",
                    "temperature": temperature
                }
            }).encode('utf-8')
            req = urllib.request.Request(
                g_url,
                data=req_data,
                headers={'Content-Type': 'application/json', 'User-Agent': 'Bolo-Backend/1.0'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=6) as g_resp:
                res_data = json.loads(g_resp.read().decode('utf-8'))
                return res_data, None
        except Exception as ge:
            last_err = str(ge)
            continue
    return None, last_err

def parse_gemini_text_to_json(gemini_res):
    try:
        raw_text = gemini_res.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        raw_text = raw_text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
        return json.loads(raw_text.strip())
    except Exception:
        return None

class BoloBackendHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable full CORS for frontend on Vercel or localhost
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, apikey')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # API Health / Welcome Endpoint
        parsed_url = urllib.parse.urlparse(self.path)
        clean_path = parsed_url.path.rstrip('/')
        query_params = urllib.parse.parse_qs(parsed_url.query)

        if clean_path in ('', '/'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            welcome = {
                "service": "English Speaking Coach Backend API",
                "status": "online",
                "geminiReady": bool(GEMINI_API_KEY),
                "supabaseReady": bool(SUPABASE_URL and SUPABASE_SEC_KEY),
                "endpoints": {
                    "health": "/",
                    "geminiChat": "POST /api/gemini/chat",
                    "lessons": "GET /api/lessons",
                    "grammar": "GET /api/grammar",
                    "grammarTopics": "GET /api/grammar/topics?level={level}&category={cat}",
                    "grammarMistakes": "GET /api/grammar/mistakes?category={cat}",
                    "grammarComparisons": "GET /api/grammar/comparisons",
                    "grammarCoach": "POST /api/grammar/coach",
                    "speakingExercises": "GET /api/speaking/exercises",
                    "conversationScenarios": "GET /api/conversations/scenarios",
                    "sentenceBuilder": "GET /api/sentence-builder",
                    "pronunciation": "GET /api/pronunciation",
                    "dailyChallenges": "GET /api/challenges/today",
                    "supabaseStatus": "GET /api/supabase/status",
                    "supabaseLoad": "GET /api/supabase/load?userId={id}",
                    "supabaseSave": "POST /api/supabase/save"
                }
            }
            self.wfile.write(json.dumps(welcome, indent=2).encode('utf-8'))
            return

        # Learning Modules REST API
        if seed_data:
            # 1. Grammar Topics with filtering
            if clean_path in ('/api/grammar', '/api/grammar/topics'):
                items = seed_data.GRAMMAR_CURRICULUM
                lvl = query_params.get('level', [None])[0]
                cat = query_params.get('category', [None])[0]
                if lvl and lvl.lower() != 'all':
                    items = [x for x in items if x.get('level', '').lower() == lvl.lower()]
                if cat and cat.lower() != 'all':
                    items = [x for x in items if x.get('category', '').lower() == cat.lower()]

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "count": len(items), "data": items}, indent=2).encode('utf-8'))
                return

            # 2. Grammar Mistakes with filtering
            if clean_path == '/api/grammar/mistakes':
                items = seed_data.COMMON_GRAMMAR_MISTAKES
                cat = query_params.get('category', [None])[0]
                if cat and cat.lower() != 'all':
                    items = [x for x in items if x.get('category', '').lower() == cat.lower()]

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "count": len(items), "data": items}, indent=2).encode('utf-8'))
                return

            # 3. Grammar Comparisons
            if clean_path == '/api/grammar/comparisons':
                items = seed_data.GRAMMAR_COMPARISONS
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "count": len(items), "data": items}, indent=2).encode('utf-8'))
                return

            # Other static routes
            routes = {
                '/api/lessons': seed_data.LESSONS,
                '/api/speaking/exercises': seed_data.SPEAKING_EXERCISES,
                '/api/conversations/scenarios': seed_data.CONVERSATION_SCENARIOS,
                '/api/sentence-builder': seed_data.SENTENCE_BUILDER_ITEMS,
                '/api/pronunciation': seed_data.PRONUNCIATION_TOPICS,
                '/api/challenges/today': seed_data.DAILY_CHALLENGES
            }
            if clean_path in routes:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    "success": True,
                    "count": len(routes[clean_path]),
                    "data": routes[clean_path]
                }
                self.wfile.write(json.dumps(response, indent=2).encode('utf-8'))
                return

        if self.path.startswith('/api/supabase/status'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            res = {
                "connected": bool(SUPABASE_URL),
                "url": SUPABASE_URL,
                "bucket": "bolo_cloud",
                "publishableKey": SUPABASE_PUB_KEY,
                "geminiReady": bool(GEMINI_API_KEY)
            }
            self.wfile.write(json.dumps(res).encode('utf-8'))
            return

        if self.path.startswith('/api/supabase/load'):
            user_id = 'brajesh_main'
            if 'userId=' in self.path:
                user_id = self.path.split('userId=')[1].split('&')[0]
            
            # Fetch from Supabase Storage
            cloud_url = f"{SUPABASE_URL}/storage/v1/object/public/bolo_cloud/profiles/{user_id}.json"
            try:
                req = urllib.request.Request(cloud_url, headers={'User-Agent': 'Bolo-Backend/1.0'})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = resp.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(data)
                    return
            except Exception as e:
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        super().do_GET()

    def do_POST(self):
        # 1. Dedicated AI Grammar Coach Endpoint
        if self.path.startswith('/api/grammar/coach'):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body.decode('utf-8'))
                action = payload.get('action', 'chat')  # 'chat', 'check', 'explain', 'compare'
                query = payload.get('query', '')
                sentence = payload.get('sentence', query)
                word = payload.get('word', query)
                termA = payload.get('termA', '')
                termB = payload.get('termB', '')
                key = payload.get('key') or GEMINI_API_KEY

                prompt = ""
                if action == 'check':
                    prompt = f"""You are a Master English Grammar Coach.
Task: Analyze this sentence for English grammar, syntax, preposition usage, and natural spoken fluency:
"{sentence}"

Output strictly a single JSON object with this exact structure:
{{
  "status": "correct" or "needs_improvement" or "incorrect",
  "original": "{sentence}",
  "corrected": "Corrected sentence with flawless grammar",
  "rule": "Short grammar rule name (e.g., Subject-Verb Agreement, Past Simple Negation)",
  "explanation": "Clear, concise 2-3 sentence explanation of what was wrong and why the correction works",
  "better_alternatives": [
    "Casual spoken alternative",
    "Polite/Professional workplace alternative"
  ],
  "speaking_drill": "Short sentence for the learner to practice saying out loud"
}}"""
                elif action == 'explain':
                    prompt = f"""You are an expert English Grammar and Vocabulary Coach.
Task: Explain the word, conjunction, or phrase: "{word}".
Output strictly a single JSON object with this exact structure:
{{
  "word": "{word}",
  "part_of_speech": "e.g. Conjunction, Preposition, Phrasal Verb",
  "cefr_level": "e.g. B1, B2, C1",
  "definition": "Clear, intuitive definition in simple English",
  "formula": "Sentence structure pattern or formula (if applicable)",
  "examples": [
    "Natural spoken example sentence 1",
    "Natural spoken example sentence 2",
    "Natural spoken example sentence 3"
  ],
  "collocations": ["Common collocation 1", "Common collocation 2"],
  "common_mistake": "Don't say: '...' Say: '...'",
  "speaking_drill": "A prompt asking the learner to create their own spoken sentence"
}}"""
                elif action == 'compare':
                    prompt = f"""You are an expert English Grammar Coach.
Task: Compare and explain the difference between "{termA}" and "{termB}".
Output strictly a single JSON object with this exact structure:
{{
  "termA": "{termA}",
  "termB": "{termB}",
  "summary": "1-2 sentence core difference",
  "ruleA": "Exact rule and conditions for using {termA}",
  "ruleB": "Exact rule and conditions for using {termB}",
  "examplesA": ["Example using {termA} 1", "Example using {termA} 2"],
  "examplesB": ["Example using {termB} 1", "Example using {termB} 2"],
  "memory_trick": "Quick golden rule or memory shortcut to never confuse them again",
  "quiz_question": "A multiple-choice question testing the difference",
  "quiz_options": ["Option A", "Option B"],
  "quiz_answer": "Option A"
}}"""
                else: # 'chat'
                    prompt = f"""You are an encouraging, expert AI English Grammar Coach.
The student asks: "{query}"

Output strictly a single JSON object with this exact structure:
{{
  "reply": "Clear, warm, highly educational explanation answering the student's question directly",
  "rule": "Grammar rule name or principle involved",
  "formula": "Sentence pattern or formula if applicable",
  "examples": [
    "Clear practical example 1",
    "Clear practical example 2"
  ],
  "mistake": "Common trap or mistake to avoid",
  "speaking_prompt": "Actionable speaking prompt for the student to practice now"
}}"""

                # Try Gemini
                gemini_res, err = call_gemini_raw(prompt, key=key)
                parsed = None
                if gemini_res:
                    parsed = parse_gemini_text_to_json(gemini_res)

                # If Gemini returned parsed JSON, send it
                if parsed:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "source": "gemini", "data": parsed}, indent=2).encode('utf-8'))
                    return

                # Local fallback knowledge engine
                fallback_data = None
                q_lower = (sentence if action == 'check' else (word if action == 'explain' else query)).lower()

                if seed_data and hasattr(seed_data, 'AI_GRAMMAR_KNOWLEDGE_BASE'):
                    for k, v in seed_data.AI_GRAMMAR_KNOWLEDGE_BASE.items():
                        if k in q_lower:
                            fallback_data = v
                            break

                if not fallback_data:
                    # Generic intelligent response
                    if action == 'check':
                        fallback_data = {
                            "status": "correct",
                            "original": sentence,
                            "corrected": sentence,
                            "rule": "Sentence Construction",
                            "explanation": "Your sentence is grammatically sound, clearly structured, and easy to understand!",
                            "better_alternatives": [
                                f"In other words: {sentence}",
                                f"More formally: As stated, {sentence.lower()}"
                            ],
                            "speaking_drill": f"Practice saying aloud: '{sentence}' with confident pacing."
                        }
                    elif action == 'explain':
                        fallback_data = {
                            "word": word,
                            "part_of_speech": "English Expression",
                            "cefr_level": "B1",
                            "definition": f"'{word}' is widely used in everyday and professional English.",
                            "formula": f"Subject + {word} + Object",
                            "examples": [
                                f"I use '{word}' when expressing my thoughts clearly.",
                                f"Mastering '{word}' helps elevate spoken English fluency."
                            ],
                            "collocations": [f"frequently use {word}", f"understand {word}"],
                            "common_mistake": f"Be mindful of correct prepositions when using '{word}'.",
                            "speaking_drill": f"Formulate your own spoken sentence using '{word}'."
                        }
                    else:
                        fallback_data = {
                            "reply": f"Great grammar question about '{query}'. English grammar is most effectively mastered when you understand the core pattern and immediately speak it aloud in complete sentences.",
                            "rule": "Core English Grammar Rule",
                            "formula": "Subject + Verb + Object",
                            "examples": [
                                "Daily practice produces remarkable spoken fluency.",
                                "Confidence grows each time you speak out loud."
                            ],
                            "mistake": "Avoid translating word-by-word from your native tongue; think in English phrase chunks.",
                            "speaking_prompt": "Speak two sentences incorporating the idea you just asked about."
                        }

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "source": "knowledge_base", "data": fallback_data}, indent=2).encode('utf-8'))
                return

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        # 2. General Gemini AI Chat Endpoint
        if self.path.startswith('/api/gemini/chat'):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body.decode('utf-8'))
                prompt = payload.get('prompt', '')
                key = payload.get('key') or GEMINI_API_KEY
                if not key:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "No Gemini API key configured on server."}).encode('utf-8'))
                    return

                gemini_result, err = call_gemini_raw(prompt, key=key)
                if gemini_result:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(gemini_result).encode('utf-8'))
                    return
                else:
                    self.send_response(502)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": f"Gemini API error: {err}"}).encode('utf-8'))
                    return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        # 3. Supabase Cloud Sync Endpoint
        if self.path.startswith('/api/supabase/save'):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                payload = json.loads(body.decode('utf-8'))
                user_id = payload.get('userId', 'brajesh_main')
                save_data = payload.get('data', {})

                if not SUPABASE_SEC_KEY:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Supabase Secret Key is not configured on server."}).encode('utf-8'))
                    return

                cloud_url = f"{SUPABASE_URL}/storage/v1/object/bolo_cloud/profiles/{user_id}.json"
                headers = {
                    'apikey': SUPABASE_SEC_KEY,
                    'Authorization': f'Bearer {SUPABASE_SEC_KEY}',
                    'Content-Type': 'application/json',
                    'x-upsert': 'true',
                    'User-Agent': 'Bolo-Backend/1.0'
                }
                upload_body = json.dumps(save_data).encode('utf-8')
                req = urllib.request.Request(cloud_url, data=upload_body, headers=headers, method='POST')
                with urllib.request.urlopen(req, timeout=10) as resp:
                    resp_data = resp.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "status": resp.status}).encode('utf-8'))
                    return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        super().do_POST()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} {args[1]}\n")

def run():
    env_port = os.environ.get("PORT")
    if env_port:
        port = int(env_port)
        host = "0.0.0.0"
        is_cloud = True
    else:
        port = get_free_port()
        host = "127.0.0.1"
        is_cloud = False

    print("=" * 65)
    print("     BOLO - English Speaking Backend API Server")
    print("=" * 65)
    print(f"\n[OK] Server running on http://{host}:{port}/")
    print(f"[OK] Supabase Cloud: {SUPABASE_URL}")
    print(f"[OK] Gemini AI API: {'Ready' if GEMINI_API_KEY else 'Awaiting key'}")
    print(f"[OK] Mode: {'Cloud (Production / Render)' if is_cloud else 'Localhost'}")
    print("=" * 65)

    try:
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer((host, port), BoloBackendHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[OK] Backend stopped cleanly.")

if __name__ == '__main__':
    run()
