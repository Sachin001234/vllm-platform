import requests


def test_chat_completion():
    payload = {
        "model": "Qwen/Qwen2.5-1.5B-Instruct-AWQ",
        "messages": [
            {
                "role": "user",
                "content": "Say hello in one short sentence."
            }
        ],
        "max_tokens": 20,
        "temperature": 0.2,
    }


