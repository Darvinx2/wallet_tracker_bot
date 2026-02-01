import re
from typing import List

import aiohttp

from infrastructure.solana_api.api_request import api_request


async def prepare_farm_data(
    user_id: int, new_wallets: List[str], session: aiohttp.ClientSession, chain: str
):
    wallets = []
    if chain == "solana":
        for wallet in new_wallets:
            if len(wallet) == 44 and wallet.isalnum():
                wallets.append(wallet)
    request = await api_request(wallets, session)
    total = float(re.search(r"Total:\s*([0-9]*\.?[0-9]+)\$", request).group(1))
    return request, wallets, total
