import os
from groq import Groq
from models import ChatMode
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def get_llm_response(message: str, mode: ChatMode):
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return f"Error: Groq API key not found. Mode selected: {mode}. Message: {message}"

    client = Groq(api_key=api_key)

    SYSTEM_PROMPTS = {
        ChatMode.teacher: "You are a patient teacher. Explain concepts simply with examples.",
        ChatMode.concise: "You are a minimalist assistant. Give extremely short, direct answers.",
        ChatMode.creative: "You are a poetic storyteller. Use metaphors and vivid imagery."
    }

    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPTS[mode]},
            {"role": "user", "content": message}
        ],
        temperature=0.7 if mode == ChatMode.creative else 0.3,
        max_tokens=100
    )
    return response.choices[0].message.content