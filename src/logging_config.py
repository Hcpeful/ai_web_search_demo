"""
logging_config.py
📚 LESSON: ENTERPRISE LOGGING
"""
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    handler = RotatingFileHandler("app.log", maxBytes=200000, backupCount=1)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[handler]
    )
    return logging.getLogger(__name__)
