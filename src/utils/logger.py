import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str):
    """Configure logger with file and console handlers"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create logs directory
    log_dir = Path(__file__).parent.parent.parent / 'logs'
    log_dir.mkdir(exist_ok=True)

    # File handler
    file_handler = RotatingFileHandler(
        log_dir / f'{name}.log',
        maxBytes=1024*1024,
        backupCount=5
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(file_handler)

    return logger