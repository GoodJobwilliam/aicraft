FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "aicraft-code-review==0.1.2" "mcp<2"

ENTRYPOINT ["mcp-code-review"]
