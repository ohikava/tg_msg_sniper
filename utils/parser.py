from telethon.tl.types import MessageEntityTextUrl
from telethon.events.newmessage import EventCommon
from loguru import logger 
from utils.types import NetworkName
from utils.funcs import format_output
from typing import List

def parse_msg(msg: str):
    for url_entity, _ in msg.get_entities_text(MessageEntityTextUrl):
        if "birdeye" in url_entity.url:
            contract_address = url_entity.url.split("token/")[1]
            return contract_address


def handle_messages(url: str, networks: List[NetworkName]): 
    async def _(event: EventCommon):
        msg = event.chat_id

        out = format_output(url, str(msg), "Solana")
        logger.info(out)
    return _ 
        