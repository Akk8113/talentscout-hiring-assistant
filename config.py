from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

EXIT_KEYWORDS = ["exit", "quit", "bye", "end"]

#OPENAI_API_KEY=your_openai_api_key


