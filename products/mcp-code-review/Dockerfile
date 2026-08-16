FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir aicraft-code-review
RUN pip install --no-cache-dir "aicraft-code-review @ git+https://github.com/GoodJobwilliam/aicraft.git@a79a6fb#subdirectory=products/mcp-code-review"

ENTRYPOINT ["mcp-code-review"]
