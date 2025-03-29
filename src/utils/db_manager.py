import sqlite3
from pathlib import Path
import logging


class DatabaseManager:
    """Handles database operations for stock data"""

    def __init__(self, db_file: str):
        """Initialize the database manager and create the database if it doesn't exist."""
        # Create data directory if it doesn't exist
        self.data_dir = Path(__file__).parent.parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)

        # Database file path
        self.db_file = self.data_dir / db_file

        # Initialize database
        self.init_database()

    def init_database(self):
        """Initialize the database with required tables"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()

                # Create stocks table
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS stocks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        symbol TEXT NOT NULL UNIQUE,
                        name TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                )

                # Create price_history table
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS price_history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        stock_id INTEGER,
                        timestamp DATETIME NOT NULL,
                        open REAL,
                        high REAL,
                        low REAL,
                        close REAL,
                        volume INTEGER,
                        FOREIGN KEY (stock_id) REFERENCES stocks (id)
                    )
                """
                )

                conn.commit()
                logging.info("Database initialized successfully")

        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
            raise
