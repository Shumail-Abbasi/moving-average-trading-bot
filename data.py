from binance.client import Client
import pandas as pd

client = Client()

def get_klines(symbol="BTCUSDT", interval="1m", limit=100):
    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    df = pd.DataFrame(klines, columns=[
        "time", "open", "high", "low", "close", "volume",
        "close_time", "qav", "num_trades",
        "taker_base_vol", "taker_quote_vol", "ignore"
    ])

    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)

    return df