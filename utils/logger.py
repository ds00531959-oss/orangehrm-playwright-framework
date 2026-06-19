import logging
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("orangehrm")
logger.setLevel(logging.INFO)

# Avoid duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler("logs/automation.log")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)