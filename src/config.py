import os
from dotenv import load_dotenv

# Load .env into environment once for the whole package
load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
