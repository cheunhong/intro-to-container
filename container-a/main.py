import logging
import time
import os

ENV = os.environ.get("ENV", "dev")

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("server.log"),
        logging.StreamHandler()
    ]
)


while True:
    logging.info(f"Info logging test for env {ENV}...")
    time.sleep(10)
