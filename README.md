# Portfolio Backend API

A production-ready Flask backend for the portfolio website. This API serves project and internship data from Firebase Firestore.

## 🚀 Features

- **REST API** for projects and internships
- **Firebase Firestore** integration with environment-based credentials
- **CORS** enabled for cross-origin requests
- **Error Handling** with standardized JSON responses
- **Modular Architecture** with Blueprints and separate services
- **Production-ready** for Render deployment

## 📁 Project Structure

```
backend/
├── app.py                      # Main Flask application
├── routes/                     # API route blueprints
│   ├── __init__.py
│   ├── health.py              # Health check endpoints
│   ├── projects.py            # Projects API routes
│   └── internships.py         # Internships API routes
├── services/                  # Business logic & integrations
│   ├── __init__.py
│   └── firebase_service.py    # Firebase initialization
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── error_handlers.py      # Error response helpers
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🔧 Setup & Installation

### Prerequisites

- Python 3.8+
- Firebase project with Firestore database
- pip (Python package manager)

### Step 1: Clone Repository

```bash
git clone <your-repo-url>
cd backend
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the backend folder:

```env
FIREBASE_KEY={"type": "service_account", "project_id": "your_project_id", "private_key_id": "...", "private_key": "...", "client_email": "...", "client_id": "...", "auth_uri": "...", "token_uri": "...", "auth_provider_x509_cert_url": "...", "client_x509_cert_url": "..."}
HOST=0.0.0.0
PORT=5000
DEBUG=False
```

**How to get FIREBASE_KEY:**
1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project → Project Settings (⚙️)
3. Go to **Service Accounts** tab
4. Click **Generate New Private Key**
5. Copy the entire JSON content as a single line
6. Paste it as the `FIREBASE_KEY` value

### Step 5: Run the Server

```bash
python app.py
```

Server will start on `http://localhost:5000`

## 📡 API Endpoints

### Health Check

```http
GET /
```

Returns server status.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Backend Running Successfully 🚀",
  "status": "online"
}
```

---

### Get All Projects

```http
GET /api/projects
```

Fetches all projects from Firestore.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Projects fetched successfully",
  "data": [
    {
      "id": "doc_id_1",
      "title": "Fraud Detection System",
      "description": "Advanced fraud detection using Graph Neural Networks",
      "tech": ["Python", "PyTorch", "GraphSAGE"],
      "image": "https://images.unsplash.com/...",
      "github": "https://github.com/...",
      "demo": "https://..."
    }
  ]
}
```

**Error Response (500):**
```json
{
  "success": false,
  "error": "Failed to fetch projects",
  "details": "error message"
}
```

---

### Get All Internships

```http
GET /api/internships
```

Fetches all internships from Firestore.

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Internships fetched successfully",
  "data": [
    {
      "id": "doc_id_1",
      "role": "Python Developer Intern",
      "company": "Infosys Springboard",
      "duration": "Oct 2024 – Dec 2024",
      "points": [
        "Led a team to develop Weather Monitoring system",
        "Built backend logic using Flask"
      ],
      "tech": ["Python", "Flask", "REST APIs"]
    }
  ]
}
```

---

## 🌐 Deployment on Render

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Prepare backend for production deployment"
git push origin main
```

### Step 2: Deploy on Render

1. Go to [render.com](https://render.com) and sign up
2. Click **"New +"** → **"Web Service"**
3. **Connect GitHub** and select your repository
4. Fill in the configuration:

   | Field | Value |
   |-------|-------|
   | **Name** | `portfolio-api` |
   | **Root Directory** | `backend` |
   | **Environment** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `python app.py` |

5. Click **"Create Web Service"**

### Step 3: Add Environment Variables on Render

1. Go to your deployed service on Render
2. Click **Settings** → **Environment**
3. Add the following variables:

   | Key | Value |
   |-----|-------|
   | `FIREBASE_KEY` | Paste your entire Firebase JSON (from Step 4 of Setup) |
   | `HOST` | `0.0.0.0` |
   | `PORT` | `5000` |
   | `DEBUG` | `False` |

4. Click **"Save Changes"** and wait for redeploy

### Step 4: Get Your Backend URL

After deployment, Render provides a URL like:
```
https://portfolio-api.onrender.com
```

Use this URL in your **frontend `.env`**:
```env
VITE_API_URL=https://portfolio-api.onrender.com
```

## 🔒 Security & Best Practices

✅ **Firebase credentials** loaded from environment variables (never hardcoded)
✅ **CORS** configured to accept frontend requests
✅ **Error handling** doesn't expose sensitive information
✅ **.env file** in `.gitignore` (never committed to GitHub)
✅ **firebase_key.json** in `.gitignore` (never committed)
✅ **Standard JSON responses** for all endpoints

## 📊 How Data Flows

```
Frontend
  ↓
GET /api/projects
  ↓
Backend (Flask)
  ↓
Query Firestore: db.collection("projects").stream()
  ↓
Firebase Firestore
  ↓
Return documents with IDs
  ↓
Backend transforms and returns JSON
  ↓
Frontend receives and displays
```

## 🛠️ Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `FIREBASE_KEY` | ✅ Yes | Firebase service account credentials | JSON string |
| `HOST` | ❌ No | Server host | `0.0.0.0` |
| `PORT` | ❌ No | Server port | `5000` |
| `DEBUG` | ❌ No | Debug mode | `False` |

## 🧪 Testing Endpoints Locally

### Using cURL

```bash
# Health check
curl http://localhost:5000/

# Get projects
curl http://localhost:5000/api/projects

# Get internships
curl http://localhost:5000/api/internships
```

### Using Postman

1. Import the following requests:
   - `GET` http://localhost:5000/
   - `GET` http://localhost:5000/api/projects
   - `GET` http://localhost:5000/api/internships

## 🐛 Troubleshooting

### Issue: "FIREBASE_KEY environment variable not set"

**Solution:**
- Create `.env` file in backend folder with FIREBASE_KEY
- Or set environment variable before running: `export FIREBASE_KEY="..."`

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"

**Solution:**
```bash
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

### Issue: CORS Error in Frontend

**Error:** `Access to XMLHttpRequest blocked by CORS policy`

**Solution:**
- Backend already has CORS enabled ✅
- Check frontend `.env` has correct `VITE_API_URL`
- Make sure backend is running and accessible

### Issue: Firebase Error on Deployment

**Solution:**
- Verify FIREBASE_KEY is set in Render environment variables
- Check that FIREBASE_KEY is valid JSON (not escaped incorrectly)
- Test locally first before deploying

## 📚 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Main Flask app, registers all blueprints |
| `routes/health.py` | Health check endpoints |
| `routes/projects.py` | Projects API endpoints |
| `routes/internships.py` | Internships API endpoints |
| `services/firebase_service.py` | Firebase initialization and configuration |
| `utils/error_handlers.py` | Error response utilities |
| `requirements.txt` | Python package dependencies |
| `.env.example` | Template for environment variables |

## 🚀 Performance Tips

- Firebase Firestore is optimized for read-heavy operations
- Responses are cached by CDN when deployed on Render
- Collection queries are limited to document size
- Consider indexing in Firestore for better query performance

## 📖 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Firebase Admin SDK](https://firebase.google.com/docs/database/admin/start)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [Render Deployment Guide](https://render.com/docs)
- [CORS Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## 📝 License

MIT License - Feel free to use this project!

---

**Built with Flask ⚡ Firebase 🔥 and Render 🚀**

Need help? Check the troubleshooting section or refer to the links above.
