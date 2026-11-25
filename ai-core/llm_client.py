import os
import json
from openai import OpenAI

# Supporta OpenAI, Groq, Ollama cambiando base_url e api_key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "mock-key"),
    base_url=os.getenv("OLLAMA_BASE_URL", "https://api.openai.com/v1")
)

def evaluate_scenario(system_prompt, user_data_json):
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini", # Cambiare a seconda del provider
            temperature=0.0,    # Massimo determinismo per la demo
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_data_json}
            ]
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"API Error: {e}")
        from fallback_mock import get_fallback_response
        return get_fallback_response()
