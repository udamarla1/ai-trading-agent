import logging
from .marketing_data import get_latest_price
from .logging_config import configure_logging


def main():
    """Main function to demonstrate fetching the latest price (safe/simulated)."""
    log_path = configure_logging()
    logger = logging.getLogger("ai-trading-agent")

    symbol = "AAPL"  # Example stock symbol
    qty = 1          # Quantity to buy/sell
    side = "buy"     # Order side: 'buy' or 'sell'

    logger.info("Starting price lookup for %s", symbol)

    # Fetch the latest price
    latest_price = get_latest_price(symbol)
    if latest_price is not None:
        logger.info("The latest price for %s is $%.2f", symbol, latest_price)
    else:
        logger.warning("Could not fetch the latest price for %s.", symbol)

    # Simulate placing a market order (do not place real orders from this demo)
    logger.info("Simulating placing a %s order for %s x%d (no real order placed)", side, symbol, qty)

    logger.info("Logs written to %s", log_path)


if __name__ == "__main__":
    main()