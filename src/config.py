from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class Config:
    """Application configuration."""
    BASE_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = BASE_DIR / 'data'
    LOG_DIR: Path = BASE_DIR / 'logs'
    DB_FILE: Path = DATA_DIR / 'stocks.db'
    
    # API Configuration
    POLYGON_API_KEY: Optional[str] = None
    API_RATE_LIMIT: int = 5
    API_TIMEOUT: int = 30
    
    # Chart Configuration
    CHART_DPI: int = 100
    CHART_STYLE: str = 'seaborn'
    CHART_FIGSIZE: tuple = (10, 6)
    
    def __post_init__(self):
        """Ensure required directories exist."""
        self.DATA_DIR.mkdir(exist_ok=True)
        self.LOG_DIR.mkdir(exist_ok=True)

config = Config()