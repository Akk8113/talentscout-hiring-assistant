import streamlit as st
import os

# Try Streamlit secrets first (cloud)
if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Otherwise use environment variable (local)
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


EXIT_KEYWORDS = ["exit", "quit", "finish", "end"]


