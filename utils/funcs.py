from typing import Dict
from utils.types import Config, Source
from telethon import TelegramClient


def load_urls(config: Config) -> Dict[str, Source]:
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

    return srcs

async def sendMessage(msg: str, receiver: str, client: TelegramClient):
    entity=await client.get_entity(receiver)
    await client.send_message(entity=entity,message=msg)