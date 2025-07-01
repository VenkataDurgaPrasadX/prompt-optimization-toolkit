# utils.py
import requests

def call_model_api(api_key, model, prompt, temperature, max_tokens):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        message = data["choices"][0]["message"]["content"] if "choices" in data else "No response"
        usage = data.get("usage", {}).get("total_tokens", "N/A")
        return {"response": message, "tokens": usage}
    except Exception as e:
        return {"response": f"Error: {str(e)}", "tokens": "N/A"}


def calculate_token_usage(prompt):
    return len(prompt.split())
