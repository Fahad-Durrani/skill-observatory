import logging
import os
from logging.handlers import RotatingFileHandler

# Get the current working directory and create a log directory
app_root = os.getcwd()
abs_root_path = os.path.abspath(app_root)
print(abs_root_path)
log_dir = os.path.join(abs_root_path, "log_dir")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, "log_file.log")
print(log_file)

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler with rotation
rotating_handler = RotatingFileHandler(
    log_file, maxBytes=5*1024*1024, backupCount=2  # 5 MB per file, up to 2 backup files
)
rotating_handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(rotating_handler)




