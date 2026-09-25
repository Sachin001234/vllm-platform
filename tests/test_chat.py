import requests

from conftest import VLLM_BASE_URL


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

    response = requests.post(
        f"{VLLM_BASE_URL}/v1/chat/completions",
        json=payload,
        timeout=60,
    )

    assert response.status_code == 200

    data = response.json()

    assert "choices" in data
    assert len(data["choices"]) > 0
    assert data["choices"][0]["message"]["content"]

