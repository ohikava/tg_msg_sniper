import os
import time 
from dotenv import load_dotenv
from telethon import TelegramClient, events
from utils import parse_msg
from observer import Observer
from sniper import Sniper 
import logging
from datetime import datetime 
import threading

load_dotenv()

logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s", level=logging.INFO, filename=f"logs/{datetime.today().strftime('%Y-%m-%d')}.txt", datefmt='%I:%M:%S', filemode='w')

logger = logging.getLogger(__name__)


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

CHAT_URL = "@GettingRich7"
ADMIN_URL = "6587260791" 

bonk = "@bonkbot_bot"
url = "https://t.me/GettingRich7"

observer = Observer()
sniper = Sniper()
client = TelegramClient('anon', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHAT_URL))
async def new_message_handler(event):
    sender_id = event.message.sender_id
            
    if str(sender_id) == ADMIN_URL:
        contract = parse_msg(event.message)

        if contract:
            observer.send_token_info(contract)
            logger.info(f"Sniping {contract}...")

            await client.send_message(bonk, contract)


def start_bot():
    client.start()
    client.run_until_disconnected()

def other_process():
    while True:
        if time.time() % 2 == 0:
            print("Even")

# threading.Thread(target=other_process).start()
start_bot()


