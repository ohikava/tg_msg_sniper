import re 
from utils.types import TokenInfo
from loguru import logger

solAddress = r"[a-zA-Z0-9]{44}"
evmAddress = r"[a-zA-Z0-9]{42}"
tonAddress = r"[a-zA-Z0-9_\-]{48}"

def extractTokenAddress(row):
    res = {
        "Ton": [],
        "Ethereum": [],
        "Base": [],
        "Solana": []
    }

    tokens = row.replace("\n", " ").split(" ")
    for t in tokens:
        for p in t.split("/"):  
            if re.fullmatch(solAddress, p):
                res['Solana'].append(p)
            elif re.fullmatch(evmAddress, p) and p.startswith("0x"):
                res['Ethereum'].append(p)
            elif re.fullmatch(tonAddress, p):
                res['Ton'].append(p)
            
    return res 

mcap_pattern = "\[(.+)/"
def extractTokenInfo(tokenInfoMessage: str) -> TokenInfo:
    res: TokenInfo = {
        "ca": "",
        "mcap": "",
        "network": ""
    }

    searchMcap = re.search(mcap_pattern, tokenInfoMessage)

    if searchMcap:
        res["mcap"] = searchMcap.group(1)
    else:
        logger.error(f"cant extract MCAP from {tokenInfoMessage}")

    addresses = extractTokenAddress(tokenInfoMessage)
    
    for key in addresses:
        if len(addresses[key]) > 0:
            res["network"] = key 
            res["ca"] = addresses[key][0]
            break 
    
    return res 
    