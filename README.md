# CVortex — AI Resume Intelligence Platform

CVortex is an AI-powered ATS Resume Optimization Platform that helps users improve their resumes for Applicant Tracking Systems (ATS) using NLP, semantic analysis, keyword intelligence, and AI-driven scoring.

---

## Live Demo

### Frontend (Streamlit)

[CVortex Live App](https://appapppy-d7w9wzicgundg3bysngw8s.streamlit.app/?utm_source=chatgpt.com)

### Backend (Render)

---

# Features

- ATS Resume Scoring
- AI-Powered Semantic Analysis
- Keyword Match Intelligence
- Component-wise Resume Breakdown
- PDF/DOCX Resume Support
- Secure Authentication with Supabase
- Analysis History Tracking
- Resume Optimization Recommendations
- Modern Animated UI
- Fast Local AI Processing

---

# Tech Stack

## Frontend

- Streamlit
- Custom CSS
- Streamlit Option Menu

## Backend

- FastAPI
- Uvicorn

## AI / NLP

- Sentence Transformers
- spaCy
- Transformers
- Scikit-learn

## Database & Auth

- Supabase

---

# Project Structure

```bash
CVortex/
│
├── backend/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── assets/
│   ├── components/
│   ├── services/
│   ├── views/
│   └── streamlit_app.py
│
├── Dataset/
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/itsakki10/CVortex.git
cd CVortex
```

---

## 2. Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux / Mac

```bash
source env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key

SENTENCE_TRANSFORMER_MODEL=all-MiniLM-L6-v2

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_service_key
SUPABASE_ANON_KEY=your_supabase_anon_key
```

---

# Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend runs on:

```bash
http://localhost:8000
```

---

# Run Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# Core Modules

## Landing Dashboard

Modern ATS optimization homepage with animated UI.

## ATS Scorer

Analyze resumes using AI-powered ATS scoring.

## Analysis History

Track and revisit previous resume analyses.

## Resources Section

ATS optimization tips and resume guidance.

---

# Security & Privacy

- Resume analysis runs securely
- Supabase authentication integration
- Sensitive files ignored using `.gitignore`
- API keys protected using environment variables

---

# Deployment

## Frontend

Deployed using:

- Streamlit Community Cloud

## Backend

Deployable on:

- Render
- Railway
- VPS

---

# Future Improvements

- AI Resume Builder
- Job Description Match Engine
- Resume Templates
- Interview Preparation Assistant
- Multi-language Resume Support

---

## Akash Mehra

- GitHub: [itsakki10 GitHub](https://github.com/itsakki10?utm_source=chatgpt.com)
- Project: [CVortex Repository](https://github.com/itsakki10/CVortex?utm_source=chatgpt.com)

---

# Support

If you liked this project:

- Star the repository
- Fork the project
- Contribute improvements

---

# License

This project is licensed under the MIT License.

---

# CVortex

> Optimize smarter. Get shortlisted faster.
