# LeadPilot AI

A lead management dashboard with a FastAPI backend, PostgreSQL database, and Gemini-powered lead analysis.

## Features

- View lead totals, high-priority leads, and average AI score
- List and create leads through the backend API
- Analyze leads and assign priority using Gemini

## Tech stack

- **Frontend:** React, Vite, Tailwind CSS
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL (Supabase supported)
- **AI:** Google Gemini API

## Requirements

- Python 3.12 or later
- Node.js and npm
- A reachable PostgreSQL database
- A Gemini API key for AI lead analysis

## Setup

### 1. Configure the backend

Open PowerShell in the project folder:

```powershell
cd backend
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `backend/.env` and add your own credentials:

```env
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DATABASE
SUPABASE_URL=https://YOUR-PROJECT.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get the database connection details and keys from your Supabase and Google AI Studio projects. URL-encode special characters in the database password if needed.

Start the backend from the `backend` directory:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The API runs at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

### 2. Start the frontend

Open a second PowerShell terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the frontend URL printed by Vite, usually `http://localhost:5173`.

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/leads/` | Get all leads |
| `POST` | `/leads/` | Create a lead |

## Security

- Never commit `backend/.env` or share its credentials.
- Keep real API keys and database passwords out of source code.
- If a credential is exposed, rotate it with its provider.
