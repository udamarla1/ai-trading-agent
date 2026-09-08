import streamlit as st
from src.marketing_data import get_latest_price

st.set_page_config(page_title="AI Trading Agent Demo", layout="centered")

st.title("AI Trading Agent — Demo")

symbol = st.text_input("Symbol", value="AAPL")
if st.button("Get latest price"):
    with st.spinner("Fetching price..."):
        price = get_latest_price(symbol)
        if price is None:
            st.warning(f"No price available for {symbol}")
        else:
            st.success(f"Latest price for {symbol}: ${price:.2f}")

st.markdown("---")
st.write("This demo reads from your Alpaca API (set ALPACA_API_KEY and ALPACA_SECRET_KEY in `.env`).")
