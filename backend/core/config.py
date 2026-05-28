import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    _ENV_PATH = Path(__file__).resolve().parents[2] / '.env'
    load_dotenv(_ENV_PATH)
except ImportError:
    pass

#api metadata
APP_TITLE='CVortex API'
APP_VERSION='1.0.0'
APP_DESCRIPTION='Analyze resumes against job descriptions using NLP + ML. Provides detailed scoring and feedback for job seekers.'

ALLOWED_ORIGINS = [
    'https://appapppy-ktwxupi73vqhjzweksze9d.streamlit.app/'
]  

#file 
MAX_FILE_SIZE_MB=5
MAX_FILE_SIZE_BYTES=MAX_FILE_SIZE_MB*1024*1024

#Supported MIME types and their short names
SUPPORTED_MIME_TYPES = {
    'application/pdf': 'pdf',
    'application/msword': 'doc',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
}

SUPPORTED_EXTENSIONS = {'.pdf', '.doc', '.docx'}

SPACY_MODEL_PRIMARY= "en_core_web_md" #better accuracy
SPACY_MODEL_SECONDARY= "en_core_web_sm" 
SENTENCE_TRANSFORMER_MODEL = os.getenv("SENTENCE_TRANSFORMER_MODEL", "all-MiniLM-L6-v2")

# Score component weights — this is business logic treated as config
SCORE_WEIGHTS = {
    "formatting": 20, "keywords": 25, "content": 25,
    "skill_validation": 15, "ats_compatibility": 15,
}

JD_KEYWORD_WEIGHT=0.6
JD_SEMANTIC_WEIGHT=0.4

try:
    import streamlit as st

    SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
    SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "")
    SUPABASE_ANON_KEY = st.secrets.get("SUPABASE_ANON_KEY", "")
    SUPABASE_JWT_SECRET = st.secrets.get("SUPABASE_JWT_SECRET", "")
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")

except Exception:

    SUPABASE_URL = os.getenv('SUPABASE_URL', '')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', '')
    SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', '')
    SUPABASE_JWT_SECRET = os.getenv('SUPABASE_JWT_SECRET', '')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
 