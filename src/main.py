import tkinter as tk
import logging
from typing import Optional

from ui.components.frames import StockGridApp
from utils.stock_data import StockDataHandler
from config import Config

class StockApplication:
    def __init__(self, config: Optional[Config] = None):
        """Initialize the stock application with configuration"""
        self.config = config or Config()
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            filename=self.config.LOG_DIR / "app.log",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        
        # Initialize handlers
        self.stock_handler = StockDataHandler(config=self.config)
        
    def run(self):
        """Run the main application"""
        root = tk.Tk()
        app = StockGridApp(root)
        root.mainloop()

def main():
    """Main entry point for the application"""
    app = StockApplication()
    
    try:
        app.run()
    except Exception as e:
        logging.error(f"Application error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()

    

"""
import tkinter as tk
import logging

from ui.components.frames import StockGridApp
from utils.stock_data import StockDataHandler


def main():
    # Initialize the database manager
    logging.basicConfig(level=logging.INFO)

    # Initialize the database manager
    stock_handler = StockDataHandler()

    # Store a stock
    stock_id = stock_handler.store_stock_data("AAPL", "Apple Inc.")
    logging.info(f"Stored stock with ID: {stock_id}")

    # Fetch all stocks
    stocks = stock_handler.fetch_stocks()
    logging.info(f"Stocks in database: {stocks}")

    # Fetch a stock by symbol
    stock = stock_handler.fetch_stock_by_symbol("AAPL")
    logging.info(f"Fetched stock: {stock}")

    # Delete a stock
    stock_handler.delete_stock(stock_id)
    logging.info(f"Deleted stock with ID: {stock_id}")

    # Fetch all stocks again
    stocks = stock_handler.fetch_stocks()
    logging.info(f"Stocks in database after deletion: {stocks}")

    # Initialize the stock data handler

    # Create the main application window
    root = tk.Tk()
    app = StockGridApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
"""