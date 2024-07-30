from utils.types import NetworkName

def format_output(url: str, ca: str, network: NetworkName) -> str:
    return f"{url} network: {network} ca: {ca}"