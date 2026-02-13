import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# ScaleDown Configuration
# =========================
SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
SCALEDOWN_BASE_URL = os.getenv("SCALEDOWN_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")


# =========================
# Groq Configuration
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
