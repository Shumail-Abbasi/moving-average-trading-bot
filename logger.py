import csv
import os

def log_trade(trade, filename="trades.csv"):
    file_exists = os.path.isfile(filename)
    print(f"The file will be created in: {os.getcwd()}")
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=trade.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(trade)