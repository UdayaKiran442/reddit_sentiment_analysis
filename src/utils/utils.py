import pandas as pd
import certifi, ssl, urllib.request

def read_csv(file_path: str) -> pd.DataFrame:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(file_path, context=ssl_context) as response:
        df = pd.read_csv(response)
        return df
        