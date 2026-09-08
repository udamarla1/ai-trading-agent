import sys
import logging
from alpaca.trading.client import TradingClient
from .config import API_KEY, SECRET_KEY


# Lazy client singleton
_client = None


def get_client():
    """Return a cached TradingClient instance, creating it if needed."""
    global _client
    if _client is None:
        api_key = API_KEY
        secret_key = SECRET_KEY
        if not api_key or not secret_key:
            raise RuntimeError("ALPACA_API_KEY or ALPACA_SECRET_KEY not set")
        _client = TradingClient(api_key, secret_key, paper=True)
    return _client


def main():
    """Safe example wrapper for connecting to Alpaca.

    This checks environment variables and avoids printing secrets.
    Copy `.env.example` to `.env` and fill in your keys before running.
    """
    api_key = API_KEY
    secret_key = SECRET_KEY

    if not api_key or not secret_key:
        print("ALPACA_API_KEY or ALPACA_SECRET_KEY not set. Copy .env.example to .env and add your keys.")
        sys.exit(1)

    try:
        client = get_client()
        account = client.get_account()
    except Exception as e:
        logging.exception("Failed to initialize Alpaca client or fetch account")
        print("Error: could not connect to Alpaca. Check your credentials and network.")
        sys.exit(1)

    # Print safe, non-secret account info
    print("Account status:", getattr(account, "status", "unknown"))
    print("Cash:", getattr(account, "cash", "unknown"))
    print("Buying power:", getattr(account, "buying_power", "unknown"))


if __name__ == "__main__":
    main()