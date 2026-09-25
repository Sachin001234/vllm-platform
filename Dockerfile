FROM vllm/vllm-openai:v0.30.0

LABEL maintainer="Sachin Pandey"
LABEL description="vLLM inference platform"

WORKDIR /app

EXPOSE 8000
