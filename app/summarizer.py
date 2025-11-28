import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def summarize_text(text: str, style: str = "brief") -> str:

    style_prompts = {
        "brief": "Summarize briefly:",
        "detailed": "Give a detailed summary:",
        "bullet": "Summarize in bullet points:"
    }

    prompt = f"{style_prompts.get(style, 'Summarize:')} {text}"

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",   # ✅ updated working model
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        if "error" in data:
            return "API Error: " + data["error"]["message"]

        return "Unexpected response: " + str(data)

    except Exception as e:
        return f"Exception: {str(e)}"
