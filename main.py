import time
from data import get_klines
from strategy import moving_average_strategy
from paper_trader import PaperTrader

symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]

trader = PaperTrader()

while True:
    for symbol in symbols:
        df = get_klines(symbol)
        signal = moving_average_strategy(df)
        price = df["close"].iloc[-1]

        print(symbol, signal, price)

        trader.process_signal(signal, price, symbol)

    trader.print_stats()

    print("Waiting 60 seconds...")
    time.sleep(60)