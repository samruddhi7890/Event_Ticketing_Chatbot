import requests
from app.config import SCALEDOWN_API_KEY, SCALEDOWN_BASE_URL, MODEL_NAME


def call_scaledown(prompt: str):

    headers = {
        "Authorization": f"Bearer {SCALEDOWN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        f"{SCALEDOWN_BASE_URL}/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return {"choices": [{"message": {"content": "ScaleDown API Error"}}]}

    return response.json()
