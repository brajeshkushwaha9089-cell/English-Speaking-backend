import http.server
import socketserver
import webbrowser
import socket
import os
import sys
import json
import urllib.request
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
        if self.path in ('/', ''):
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
            routes = {
                '/api/lessons': seed_data.LESSONS,
                '/api/grammar': seed_data.GRAMMAR_TOPICS,
                '/api/speaking/exercises': seed_data.SPEAKING_EXERCISES,
                '/api/conversations/scenarios': seed_data.CONVERSATION_SCENARIOS,
                '/api/sentence-builder': seed_data.SENTENCE_BUILDER_ITEMS,
                '/api/pronunciation': seed_data.PRONUNCIATION_TOPICS,
                '/api/challenges/today': seed_data.DAILY_CHALLENGES
            }
            clean_path = self.path.split('?')[0].rstrip('/')
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
        # 1. Gemini AI Chat Endpoint
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

                models = ["gemini-3.5-flash", "gemini-3.1-flash-lite", "gemini-3.8-flash"]
                last_err = None
                gemini_result = None

                for model in models:
                    try:
                        g_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
                        req_data = json.dumps({
                            "contents": [{"parts": [{"text": prompt}]}],
                            "generationConfig": {
                                "responseMimeType": "application/json",
                                "temperature": 0.7
                            }
                        }).encode('utf-8')
                        req = urllib.request.Request(
                            g_url,
                            data=req_data,
                            headers={'Content-Type': 'application/json', 'User-Agent': 'Bolo-Backend/1.0'},
                            method='POST'
                        )
                        with urllib.request.urlopen(req, timeout=15) as g_resp:
                            gemini_result = json.loads(g_resp.read().decode('utf-8'))
                            break
                    except Exception as ge:
                        last_err = str(ge)
                        continue

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
                    self.wfile.write(json.dumps({"error": f"Gemini API error: {last_err}"}).encode('utf-8'))
                    return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
                return

        # 2. Supabase Cloud Sync Endpoint
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
