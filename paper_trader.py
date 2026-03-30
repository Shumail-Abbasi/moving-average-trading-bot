from logger import log_trade

class PaperTrader:
    def __init__(self, starting_balance=1000, risk_per_trade=0.1):
        self.balance = starting_balance
        self.risk_per_trade = risk_per_trade

        self.positions = {}
        self.entry_prices = {}
        self.position_sizes = {}

        self.trade_id = 0

        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0

    def process_signal(self, signal, price, symbol):
        position = self.positions.get(symbol)

        # No open position
        if position is None:
            if signal == "BUY":
                self.open_position(symbol, "LONG", price)
            elif signal == "SELL":
                self.open_position(symbol, "SHORT", price)

        # LONG open
        elif position == "LONG":
            if signal == "SELL":
                self.close_position(symbol, price)

        # SHORT open
        elif position == "SHORT":
            if signal == "BUY":
                self.close_position(symbol, price)

    def open_position(self, symbol, position_type, price):
        position_size = self.balance * self.risk_per_trade

        self.positions[symbol] = position_type
        self.entry_prices[symbol] = price
        self.position_sizes[symbol] = position_size

        print(f"Opened {position_type} on {symbol} at {price}")

    def close_position(self, symbol, price):
        self.trade_id += 1

        position = self.positions[symbol]
        entry_price = self.entry_prices[symbol]
        position_size = self.position_sizes[symbol]

        if position == "LONG":
            profit = (price - entry_price) * position_size / entry_price
        else:
            profit = (entry_price - price) * position_size / entry_price

        self.balance += profit

        self.total_trades += 1
        if profit > 0:
            self.winning_trades += 1
        else:
            self.losing_trades += 1

        trade = {
            "trade_id": self.trade_id,
            "symbol": symbol,
            "position": position,
            "entry_price": entry_price,
            "exit_price": price,
            "profit": profit,
            "balance": self.balance
        }

        log_trade(trade)

        print(f"Closed {position} on {symbol} Profit: {profit}")
        print(f"Balance: {self.balance}")

        self.positions[symbol] = None
        self.entry_prices[symbol] = 0
        self.position_sizes[symbol] = 0

    def print_stats(self):
        if self.total_trades == 0:
            return

        win_rate = (self.winning_trades / self.total_trades) * 100

        print("------ STATS ------")
        print("Total Trades:", self.total_trades)
        print("Winning Trades:", self.winning_trades)
        print("Losing Trades:", self.losing_trades)
        print("Win Rate:", round(win_rate, 2), "%")
        print("Balance:", round(self.balance, 2))
        print("-------------------")