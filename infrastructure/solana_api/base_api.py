import logging
from abc import ABC
from typing import Any, Mapping

import aiohttp

logger = logging.getLogger("base_api")
logger.setLevel(logging.INFO)


class BaseApiClient(ABC):
    async def handler_response(
        self, response: aiohttp.ClientResponse, api_name: str
    ) -> Mapping[str, Any]:
        try:
            data = await response.json()
        except Exception as e:
            logger.error(f"{api_name} error {response.status}: {e}")
            raise Exception(f"{api_name}: Error {response.status}")
