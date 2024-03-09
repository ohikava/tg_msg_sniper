import os 
from dotenv import load_dotenv
from telethon import TelegramClient, events
from utils import parse_msg
from observer import Observer
from sniper import Sniper 
import logging
import datetime 

load_dotenv()

logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s", level=logging.INFO, filename=f"logs/{datetime.today().strftime('%Y-%m-%d')}.txt", datefmt='%I:%M:%S', filemode='w')

logger = logging.getLogger(__name__)


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

CHAT_URL = "@GettingRich7"
ADMIN_URL = "6587260791" 

url = "https://t.me/GettingRich7"
observer = Observer()
sniper = Sniper()
client = TelegramClient('anon', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHAT_URL))
async def new_message_handler(event):
    print(f"New message in chat {event.chat_id}: {event.message.text}")

    sender_id = event.message.sender_id
            
    if str(sender_id) == ADMIN_URL:
        contract = parse_msg(event.message)

        if contract:
            observer.send_token_info(contract)
            logger.info(f"Sniping {contract}...")



client.start()
client.run_until_disconnected()

