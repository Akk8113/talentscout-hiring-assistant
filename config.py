import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = None

# Try Streamlit secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

# Fallback to .env
if GROQ_API_KEY is None:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

EXIT_KEYWORDS = ["exit", "quit", "finish", "end"]