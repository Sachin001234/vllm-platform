from conftest import REQUEST_TIMEOUT, VLLM_BASE_URL


def test_vllm_configuration():
    assert VLLM_BASE_URL.startswith("http://")
    assert REQUEST_TIMEOUT > 0
