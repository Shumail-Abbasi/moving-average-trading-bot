# moving-average-trading-bot

# 📈 AI Paper Trading Bot (Crypto)

## Overview
This project is a **multi-asset crypto paper trading bot** built in Python. It simulates real trading using live market data from Binance without risking actual capital. It is designed as a foundational tool for learning algorithmic trading systems step-by-step.

**The bot performs the following cycle:**
1. **Fetch:** Pulls real-time crypto price data via API.
2. **Analyze:** Generates trading signals using a modular strategy engine.
3. **Execute:** Performs simulated trades (paper trading).
4. **Manage:** Applies risk management (Stop Loss/Take Profit).
5. **Log:** Tracks performance and trade history in real-time.

---

## 🚀 Features

### Core Trading System
* **Multi-symbol Support:** Trade BTC, ETH, and SOL simultaneously.
* **Live Data:** Integration with Binance for real-time market snapshots.
* **Automated Loop:** Continuous execution with a configurable heartbeat (default: 60s).

### Strategy Engine
* **Moving Average Crossover:** A classic trend-following strategy.
* **Signal Logic:** Generates `BUY`, `SELL`, or `HOLD` directives based on technical indicators.

### Paper Trading Engine
* **Directional Trading:** Supports both **LONG** (profit on rise) and **SHORT** (profit on fall) positions.
* **Metric Tracking:** Records entry/exit prices, net profit/loss, and shifting account balance.

### Risk Management
* **Position Sizing:** Allocates a specific % of balance per trade.
* **Hard Stops:** Default Stop Loss at `-0.5%` and Take Profit at `+1.0%`.
* **Cooldown Timer:** Prevents overtrading by enforcing a 10-minute wait between trades per symbol.

### Logging & Analytics
* **Data Persistence:** All trades are saved to `trades.csv`.
* **Performance Metrics:** Calculates win rate, total trades, and balance growth curves.

---

## 🧠 Architecture
The bot follows a professional decoupled architecture to ensure scalability:

`Market Data` → `Strategy` → `Signal` → `Paper Trader` → `Risk Management` → `Logger` → `Stats`

---

## 📂 Project Structure
```text
trading_bot/
│
├── main.py            # Main execution loop
├── data.py            # Binance API integration
├── strategy.py        # Technical indicators & signal logic
├── paper_trader.py    # Simulated execution & risk rules
├── logger.py          # CSV handling & performance tracking
└── trades.csv         # Local trade database
```
---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone [https://github.com/yourusername/trading-bot.git](https://github.com/yourusername/trading-bot.git)
cd trading-bot
