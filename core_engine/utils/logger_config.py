"""Logger setup for DocGen"""

import logging

def setup_logger(name="docgen", level="INFO"):
    """
    Creates and returns a logger with the specified level.
    'level' can be a string such as 'INFO', 'DEBUG', etc.
    """
    logger = logging.getLogger(name)

    # If level is string, convert to numeric value
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    logger.setLevel(level)

    if not logger.handlers:
        ch = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
