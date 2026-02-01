from typing import List

import aiohttp

from infrastructure.solana_api.formatting import formatting
from infrastructure.solana_api.jupiter_api import JupiterPrice
from infrastructure.solana_api.moralis_api import MoralisPortfolio


async def api_request(wallets: List[str], session: aiohttp.ClientSession) -> str:
    output_message = ""
    total = 0
    for address in wallets:
        if len(address) == 44 and address.isalnum():
            try:
                moralis = MoralisPortfolio(session, address)
                tokens = await moralis.get_tokens()
                jupiter = JupiterPrice(session, tokens)
                wallet = await jupiter.tokens_info()
                result, total_on_wallet = await formatting(wallet)
                total += total_on_wallet
                output_message += f"{address}\n{result}\n"
            except Exception as e:
                return f"Error API requests: {e}"
    final_total = round(total, 2)
    output_message += str(f"Total: {final_total}$")
    return output_message if output_message else "Это не Solana кошельки 🙊"
