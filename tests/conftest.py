import os


VLLM_BASE_URL = os.getenv("VLLM_BASE_URL", "http://localhost:8000")
REQUEST_TIMEOUT = 60

