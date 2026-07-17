import requests
import os

api_key = os.environ.get("ANTHROPIC_API_KEY")


def ask_llm(prompt):
    if api_key is None:
        print("No API Key Found")
        return None
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": api_key,
    }
    body = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 100,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }
    try:
        response = requests.post(url, headers=headers, json=body)
    except requests.exceptions.ConnectionError:
        print("Could not reach the server")
        return None
    if response.status_code == 200:
        data = response.json()
        return data['content'][0]['text']
    else:
        print(response.status_code, response.text)
        return None

answer = ask_llm("test")
print(answer)