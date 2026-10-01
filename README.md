# ⚙️ Bolo English - Backend API Service

Lightweight Python backend API service providing Gemini AI voice conversation proxy and Supabase Cloud storage persistence with full CORS support.

---

## 🛠️ Tech Stack & Endpoints

- **Runtime**: Python 3 (Standard Library - zero external dependencies)
- **CORS**: Enabled for all web origins (`*`)
- **Endpoints**:
  - `GET /`: Health check & API status
  - `POST /api/gemini/chat`: Proxies Gemini AI requests to protect API keys
  - `GET /api/supabase/status`: Supabase connection status
  - `GET /api/supabase/load?userId=...`: Load user profile & data from Supabase
  - `POST /api/supabase/save`: Save user profile & data to Supabase Storage bucket

---

## 🚀 Deploy to Render

1. Go to [render.com](https://render.com) and click **New +** -> **Web Service**.
2. Connect your GitHub repository: `English-Speaking-backend`.
3. Set:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt` (or leave empty)
   - **Start Command**: `python server.py`
4. Add **Environment Variables**:
   - `GEMINI_API_KEY`: *(Your Google Gemini API Key)*
   - `SUPABASE_URL`: `https://jyatlsllsdmtdmvohhfz.supabase.co`
   - `SUPABASE_PUB_KEY`: `sb_publishable_Zku7v5nercpKO4wraLHT_A_LNSOGXih`
   - `SUPABASE_SEC_KEY`: *(Your Supabase Secret Key)*
5. Click **Deploy Web Service**!

---

## 💻 Local Running

```bash
python server.py
```
Backend will start on `http://127.0.0.1:8000/`.
