
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datetime

def render_market_feed():
    st.subheader("Live Market Feed & Analysis")

    symbol = st.selectbox("Select Crypto Pair", ["BTC/USDT", "ETH/USDT", "BNB/USDT"])
    now = datetime.datetime.now()

    st.markdown(f"**Selected Symbol:** {symbol}")
    st.markdown(f"*Last updated: {now.strftime('%Y-%m-%d %H:%M:%S')}*")

    # Simulated live prices
    price_data = pd.DataFrame({
        'time': pd.date_range(end=pd.Timestamp.now(), periods=30, freq='min'),
        'price': np.random.normal(loc=20000 if symbol == "BTC/USDT" else 1400, scale=30, size=30)
    })

    st.metric("Live Price", f"${round(price_data['price'].iloc[-1], 2)}")

    # Plot
    fig = go.Figure(data=[go.Scatter(x=price_data['time'], y=price_data['price'], mode='lines+markers')])
    fig.update_layout(title="Price Chart", xaxis_title="Time", yaxis_title="Price", height=400)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Indicators")
    sma = price_data['price'].rolling(window=5).mean()
    rsi = 100 - (100 / (1 + price_data['price'].pct_change().rolling(5).mean()))

    st.line_chart(pd.DataFrame({
        "SMA (5)": sma,
        "RSI (est)": rsi
    }))
