from typing import TypedDict, List
from enum import Enum

class NetworkName(Enum):
    SOLANA = "Solana"
    ETHEREUM = "Ethereum"
    BASE = "Base"
    TON = "Ton"


class NetworkConfig(TypedDict):
    network: NetworkName
    channels_urls: List[str]
    chat_urls: List[List[str]]
    tg_bots: List[str]

class Config(TypedDict):
    networks: List[NetworkConfig]

class Source(TypedDict):
    networks: List[NetworkName]
    whitelist: List[int]
