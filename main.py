from time import sleep
from telethon import TelegramClient, events
from loguru import logger
from telethon.events.newmessage import EventCommon
from typing import List
from dotenv import dotenv_values
import tomllib

from utils.funcs import load_urls 
from utils.types import Config, NetworkName, State
from utils.sniper import Sniper
from utils.parser import extractTokenAddress, extractTokenInfo

with open("config.toml", "rb") as f:
    config: Config = tomllib.load(f)

secrets = dotenv_values(".env")
API_ID = secrets["API_ID"]
API_HASH = secrets["API_HASH"]
TG_TOKEN = secrets["TG_TOKEN"]

srcs = load_urls(config)


client = TelegramClient('anon', API_ID, API_HASH)
sniper = Sniper(config, client)

seen = set()

def handle_messages(url: str, networks: List[NetworkName]): 
    async def _(event: EventCommon):
        msg = event.raw_text

        if "New Dexscreener Paid Token!" in msg:
            CA = msg.split("CA: ")[1].split("\n")[0]

            if CA in seen:
                return 
            
            MCAP = msg.split("Market Cap: $")[1].split("\n")[0]
            try:
                MCAP = float(MCAP.strip())

                if MCAP < 20_000:
                    return 
                
            except:
                logger.error(f"error while checking MCAP: {CA} ${MCAP}")
                return 
            

            out = f"BUY {url} {"Solana"} {CA}"
            logger.info(out)
            seen.add(CA)
            await sniper.snipe(CA, NetworkName.SOLANA)
            sleep(config['sleepAfterTXSec'])

    return _ 

for url, url_confing in srcs.items():
    msg_handles = handle_messages(url, url_confing['networks'])
    msg_handles = client.on(events.NewMessage(chats=[url]))(msg_handles)
    logger.info(f"init {url} {url_confing['networks']}")

# @client.on(events.NewMessage(chats=[config['sniperBotNickname']]))
# async def monitorSniperBot(event):
#     if global_variables['state'] == State.WAITING_FOR_TOKEN_BUY:
#         global_variables['state'] = State.NOTHING


def start_bot():
    client.start()
    client.run_until_disconnected()

start_bot()
