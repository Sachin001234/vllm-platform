import requests


def test_model_available():
    response = requests.get("http://localhost:8000/v1/models")

    assert response.status_code == 200

    data = response.json()
    models = [model["id"] for model in data["data"]]

    assert "Qwen/Qwen2.5-1.5B-Instruct-AWQ" in models
