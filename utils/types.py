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
    sleepAfterTXSec: int
    waitTimeSec: int
    waitUntilSec: int
    sniperBotNickname: str 
    loggingChannelURI: str
    tokenInfoBotNickname: str


class Source(TypedDict):
    networks: List[NetworkName]
    whitelist: List[int]

class TokenInfo(TypedDict):
    mcap: str
    network: str 
    ca: str


class State(Enum):
    NOTHING = "NOTHING"
    WAITING_FOR_TOKEN_INFO = "WAITING_FOR_TOKEN_INFO"
    WAITING_FOR_TOKEN_BUY = "WAITING_FOR_TOKEN_BUY"

class GlobalVariables(TypedDict):
    state: State