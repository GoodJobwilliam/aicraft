"""
Async HTTP client wrapper using httpx.
"""
from typing import Optional

import httpx
from core.config import Settings
from core.logger import get_logger

logger = get_logger(__name__)


class APIClient:
    """
    Reusable HTTP client with retry logic and logging.
    """

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.settings.api_base_url,
                timeout=httpx.Timeout(self.settings.api_timeout),
                follow_redirects=True,
            )
        return self._client

    async def get(
        self, path: str, params: dict | None = None
    ) -> httpx.Response:
        """GET request with retry logic."""
        client = await self._get_client()
        last_error: Exception | None = None

        for attempt in range(self.settings.api_max_retries):
            try:
                logger.info("http.get", path=path, attempt=attempt + 1)
                response = await client.get(path, params=params)
                response.raise_for_status()
                logger.info("http.get.ok", path=path, status=response.status_code)
                return response
            except (httpx.HTTPError, httpx.TimeoutException) as exc:
                last_error = exc
                logger.warning(
                    "http.get.retry",
                    path=path,
                    attempt=attempt + 1,
                    error=str(exc),
                )
                if attempt < self.settings.api_max_retries - 1:
                    import asyncio

                    await asyncio.sleep(2**attempt)  # Exponential backoff

        raise RuntimeError(f"Request failed after {self.settings.api_max_retries} retries") from last_error

    async def close(self) -> None:
        if self._client and not self._client.is_closed:
            await self._client.aclose()
