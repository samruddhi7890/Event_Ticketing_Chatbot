import requests
from app.config import GROQ_API_KEY, GROQ_BASE_URL, GROQ_MODEL


def call_groq(prompt: str):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        f"{GROQ_BASE_URL}/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return {"choices": [{"message": {"content": "Groq API Error"}}]}

    return response.json()
