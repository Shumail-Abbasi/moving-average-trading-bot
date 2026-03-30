def moving_average_strategy(df):
    df["fast_ma"] = df["close"].rolling(window=5).mean()
    df["slow_ma"] = df["close"].rolling(window=20).mean()

    last_row = df.iloc[-1]
    prev_row = df.iloc[-2]

    if prev_row["fast_ma"] < prev_row["slow_ma"] and last_row["fast_ma"] > last_row["slow_ma"]:
        return "BUY"

    elif prev_row["fast_ma"] > prev_row["slow_ma"] and last_row["fast_ma"] < last_row["slow_ma"]:
        return "SELL"

    else:
        return "HOLD"