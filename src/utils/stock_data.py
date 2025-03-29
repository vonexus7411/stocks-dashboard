import sqlite3
import logging
from typing import Optional
from config import Config
from pathlib import Path


from utils.db_manager import DatabaseManager


class StockDataHandler:
    """Handles operations related to stock data and price history"""

    def __init__(self, config: Optional[Config] = None):
        """Initialize the stock data handler with a database manager"""
        self.config = config or Config()
        self.db_manager = DatabaseManager(self.config.DB_FILE)

    def store_stock_data(self, symbol: str, name: str):
        """Store stock information"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT OR REPLACE INTO stocks (symbol, name) VALUES (?, ?)",
                    (symbol, name),
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error storing stock data: {e}")
            raise

    def store_price_history(self, stock_id: int, price_data: list):
        """Store price history data"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.executemany(
                    """
                    INSERT INTO price_history (stock_id, timestamp, open, high, low, close, volume)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    [(stock_id, *data) for data in price_data],
                )
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error storing price history: {e}")
            raise

    def fetch_price_history(self, stock_id: int):
        """Fetch price history data"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT timestamp, open, high, low, close, volume
                    FROM price_history
                    WHERE stock_id = ?
                    """,
                    (stock_id,),
                )
                return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error fetching price history: {e}")
            raise

    def fetch_stocks(self):
        """Fetch all stocks from the database"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM stocks")
                return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error fetching stocks: {e}")
            raise

    def fetch_stock_by_symbol(self, symbol: str):
        """Fetch a stock by its symbol"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))
                return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error fetching stock by symbol: {e}")
            raise

    def delete_stock(self, stock_id: int):
        """Delete a stock from the database"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM stocks WHERE id = ?", (stock_id,))
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting stock: {e}")
            raise

    def delete_price_history(self, stock_id: int):
        """Delete price history for a stock"""
        try:
            with sqlite3.connect(self.db_manager.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM price_history WHERE stock_id = ?", (stock_id,)
                )
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting price history: {e}")
            raise


"""
# Example usage of Polygon API
client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))
ticker = "SSP"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)""
"""
