import requests

from conftest import VLLM_BASE_URL


def test_vllm_health():
    response = requests.get(f"{VLLM_BASE_URL}/health")

    assert response.status_code == 200
