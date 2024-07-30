import os
import time 
from telethon import TelegramClient, events
from observer import Observer
from sniper import Sniper 
from loguru import logger
from utils.types import Config, Source
from typing import Dict
from utils.parser import handle_messages
from dotenv import dotenv_values
import tomllib

with open("config.toml", "rb") as f:
    config: Config = tomllib.load(f)

# print(config)
# channels_urls = config['channels_urls']
# networks = config['networks']
# chat_urls = defaultdict(list)

# for chat in config['chat_urls']:
#     if len(chat) > 1:
#         chat_urls[chat[0]].append(chat[1])

srcs: Dict[str, Source] = {}

for item in config['networks']:

    for url in item['channels_urls']:
        if url not in srcs:
            srcs[url] = {
                "networks": [],
                "whitelist": []
            }
        if item['network'] not in srcs[url]['networks']:
            srcs[url]['networks'].append(item['network'])
    
    for chat_config in item['chat_urls']:
        url = chat_config[0]
        if url not in srcs:
            srcs[url] = {
                "networks": [],
                "whitelist": []
            }


        if item['network'] not in srcs[url]['networks']:
            srcs[url]['networks'].append(item['network'])

        if len(chat_config) > 1 and chat_config[1]:
            srcs[url]['whitelist'].append(int(chat_config[1]))

print(srcs)




secrets = dotenv_values(".env")
API_ID = secrets["API_ID"]
API_HASH = secrets["API_HASH"]

client = TelegramClient('anon', API_ID, API_HASH)

for url, url_confing in srcs.items():
    msg_handles = handle_messages(url, url_confing['networks'])
    msg_handles = client.on(events.NewMessage(chats=[url]))(msg_handles)
    logger.info(f"init {url} {url_confing['networks']}")

def start_bot():
    client.start()
    client.run_until_disconnected()

# # def other_process():
# #     while True:
# #         if time.time() % 2 == 0:
# #             print("Even")

# # # threading.Thread(target=other_process).start()
start_bot()


