from utils.types import NetworkName, GlobalVariables, State, Config
from utils.funcs import sendMessage
from telethon import TelegramClient
from loguru import logger
import asyncio
import time

class Sniper:
    def __init__(self, config: Config, client: TelegramClient) -> None:
        self.sniperBotUrl = config['sniperBotNickname']
        self.tokenInfoBot = config['tokenInfoBotNickname']
        self.client = client 
        self.config = config 
        
    async def snipeSolana(self, CA: str):
        try:
            await sendMessage(CA, self.sniperBotUrl, self.client)
        except Exception as err:
            logger.error(f"tryied to buy {CA}, got following error")
            logger.exception(err)
            return 

    async def snipe(self, CA: str, net: NetworkName):
        if net == NetworkName.SOLANA:
            await self.snipeSolana(CA)