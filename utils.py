from telethon.tl.types import MessageEntityTextUrl

def parse_msg(msg: str):
    for url_entity, _ in msg.get_entities_text(MessageEntityTextUrl):
        if "birdeye" in url_entity.url:
            contract_address = url_entity.url.split("token/")[1]
            return contract_address