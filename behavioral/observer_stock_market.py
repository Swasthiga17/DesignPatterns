from abc import ABC, abstractmethod
from typing import List
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class StockObserver(ABC):
    @abstractmethod
    def update(self, stock_symbol: str, price: float, output_file=None):
        pass

class Stock:
    def __init__(self, symbol: str, initial_price: float):
        self.symbol = symbol
        self._price = initial_price
        self._observers: List[StockObserver] = []
    
    def add_observer(self, observer: StockObserver):
        self._observers.append(observer)
    
    def remove_observer(self, observer: StockObserver):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def set_price(self, new_price: float, output_file=None):
        old_price = self._price
        self._price = new_price
        if old_price != new_price:
            self._notify_observers(output_file)
    
    def _notify_observers(self, output_file=None):
        for observer in self._observers:
            observer.update(self.symbol, self._price, output_file)

class MobileApp(StockObserver):
    def __init__(self, app_name: str):
        self.app_name = app_name
    
    def update(self, stock_symbol: str, price: float, output_file=None):
        message = f"[{self.app_name}] Stock {stock_symbol} price updated: ${price:.2f}"
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)

class TradingBot(StockObserver):
    def update(self, stock_symbol: str, price: float, output_file=None):
        if price > 150:
            message = f"[TradingBot] Selling {stock_symbol} at high price ${price:.2f}"
        elif price < 100:
            message = f"[TradingBot] Buying {stock_symbol} at low price ${price:.2f}"
        else:
            message = f"[TradingBot] Monitoring {stock_symbol} at ${price:.2f}"
        
        if output_file:
            output_file.write(message + "\n")
        else:
            print(message)

def demo_observer(results_dir="results"):
    os.makedirs(results_dir, exist_ok=True)
    
    with open(f"{results_dir}/observer_stock_market.txt", "w") as f:
        f.write("=== Observer Pattern: Stock Market ===\n")
        
        apple_stock = Stock("AAPL", 145.50)
        google_stock = Stock("GOOGL", 2750.00)
        
        mobile_app = MobileApp("StockTracker Pro")
        trading_bot = TradingBot()
        
        apple_stock.add_observer(mobile_app)
        apple_stock.add_observer(trading_bot)
        google_stock.add_observer(mobile_app)
        
        f.write("Initial stock prices set\n")
        f.write("Simulating price changes...\n\n")
        
        apple_stock.set_price(148.75, f)
        apple_stock.set_price(152.30, f)
        google_stock.set_price(2800.50, f)
        apple_stock.set_price(95.80, f)
        
        f.write("\nObserver pattern demonstration completed successfully!\n")

if __name__ == "__main__":
    demo_observer()