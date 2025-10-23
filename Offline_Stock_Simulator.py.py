import time
import random
from datetime import datetime

stocks = {
    "AAPL": 230.0,
    "MSFT": 415.0,
    "GOOGL": 180.0
}

def display_dashboard():
    print("=" * 45)
    print("📊 OFFLINE STOCK MARKET SIMULATION DASHBOARD")
    print("=" * 45)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    for symbol, price in stocks.items():
        change_percent = random.uniform(-2, 2)
        new_price = price * (1 + change_percent / 100)
        stocks[symbol] = round(new_price, 2)
        change_value = new_price - price
        print(f"{symbol:6s}  Price: {new_price:8.2f} USD  "
              f"Change: {change_value:+6.2f} ({change_percent:+5.2f}%)")
    print("-" * 45)

def main():
    refresh = int(input("Enter refresh interval (seconds): "))
    print("\nStarting offline simulation... Press Ctrl+C to stop.\n")
    try:
        while True:
            display_dashboard()
            time.sleep(refresh)
    except KeyboardInterrupt:
        print("\nSimulation stopped. Goodbye!")

if __name__ == "__main__":
    main()