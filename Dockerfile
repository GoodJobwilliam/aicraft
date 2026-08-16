FROM python:3.12-slim

WORKDIR /app

COPY products/mcp-code-review /app
RUN pip install --no-cache-dir .

ENTRYPOINT ["mcp-code-review"]
