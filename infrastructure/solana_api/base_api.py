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
            logger.error(f"{api_name} error: {e}")
            raise Exception("Возникла ошибка парсинга")
        if response.status == 400:
            logger.error(f"{api_name}: Error 400")
            raise Exception(f"{api_name}: Error 400")
        elif response.status == 401:
            logger.error(f"{api_name}: Error 401")
            raise Exception(f"{api_name}: Error 401")
        elif response.status == 404:
            logger.error(f"{api_name}: Error 404")
            raise Exception(f"{api_name}: Error 404")
        elif response.status == 429:
            logger.error(f"{api_name}: Error 429")
            raise Exception(f"{api_name}: Error 429")
        elif response.status == 500:
            logger.error(f"{api_name}: Error 500")
            raise Exception(f"{api_name}: Error 500")
        elif response.status == 200:
            logger.info(f"{api_name}: Status 200")
            return data
        else:
            logger.error(f"{api_name}: Status {response.status}")
            raise Exception(f"Неожиданный статус: {response.status}")
