import requests

from conftest import REQUEST_TIMEOUT, VLLM_BASE_URL


def test_model_available():
    response = requests.get(
        f"{VLLM_BASE_URL}/v1/models",
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200

    data = response.json()
    models = [model["id"] for model in data["data"]]

    assert "Qwen/Qwen2.5-1.5B-Instruct-AWQ" in models
