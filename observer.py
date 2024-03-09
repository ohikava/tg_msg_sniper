import logging 
import requests 

logger = logging.getLogger(__name__)

client_id=-1002009923614
token = "6827720178:AAGyGWS3m0-0VlSujJvqekpUIhWeZtpvuzA"

class Observer:
    def send_sync_message(self, msg):
        uri = f"https://api.telegram.org/bot{token}/sendMessage"
        body = {
            "chat_id": client_id,
            "text": msg
        }
        return requests.post(uri, json=body)

    def send_token_info(self, contract: str):
        self.send_sync_message(f"Sniping {contract}...")
    
