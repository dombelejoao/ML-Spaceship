import logging
import os

class SingletonLogger:
    """
    Singleton Logger class that provides a centralized logging mechanism.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.initialize_logger()
        return cls._instance

    def initialize_logger(self):
        """
        Initialize the logger with the appropriate configuration.
        """
        logging.basicConfig(
            filename='./data/log_file.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def log(self, level, message):
        """
        Log a message with the specified level.
        """
        if level == 'info':
            logging.info(message)
        elif level == 'warning':
            logging.warning(message)
        elif level == 'error':
            logging.error(message)
        elif level == 'critical':
            logging.critical(message)