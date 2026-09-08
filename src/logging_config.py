import logging
from logging.handlers import RotatingFileHandler
import os


def configure_logging(log_dir: str = "logs", log_file: str = "app.log", level=logging.INFO):
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    file_handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root = logging.getLogger()
    if root.handlers:
        root.handlers = []
    root.setLevel(level)
    root.addHandler(file_handler)
    root.addHandler(stream_handler)

    # Return the log file path for verification
    return log_path
