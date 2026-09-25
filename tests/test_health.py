import requests

from conftest import REQUEST_TIMEOUT, VLLM_BASE_URL


def test_vllm_health():
    response = requests.get(
        f"{VLLM_BASE_URL}/health",
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 200
