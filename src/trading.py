from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from .alpaca_client import get_client

def place_market_order(symbol: str, qty: int, side: str):
    """Place a market order for a given stock symbol."""
    order_request = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY if side.lower() == "buy" else OrderSide.SELL,
        time_in_force=TimeInForce.DAY
    )
    try:
        client = get_client()
        order = client.submit_order(order_request)
        return order
    except Exception as e:
        print(f"Error placing order: {e}")
        return None