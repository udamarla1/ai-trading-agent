from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

from .config import API_KEY, SECRET_KEY

data_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)

def get_latest_price(symbol: str):
    """Fetch the latest price for a given stock symbol."""
    request_params = StockLatestQuoteRequest(symbol_or_symbols=symbol)
    latest_quote = data_client.get_stock_latest_quote(request_params)
    return latest_quote[symbol].ask_price if symbol in latest_quote else None