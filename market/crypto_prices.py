
import streamlit as st
import requests

def get_crypto_price(coin_id="bitcoin", vs_currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={vs_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[coin_id][vs_currency]
    except Exception as e:
        st.error("Failed to fetch price data.")
        return None

def render_crypto_prices():
    st.subheader("Live Crypto Prices (via CoinGecko)")

    coins = {
        "Bitcoin (BTC)": "bitcoin",
        "Ethereum (ETH)": "ethereum",
        "BNB": "binancecoin",
        "Solana (SOL)": "solana"
    }

    selected = st.selectbox("Select Coin", list(coins.keys()))
    coin_id = coins[selected]

    price = get_crypto_price(coin_id)
    if price:
        st.metric(label=f"{selected} Price", value=f"${price:,.2f}")
