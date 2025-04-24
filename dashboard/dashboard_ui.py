
import streamlit as st
import pandas as pd
import os
from bot_engine.bot_ui import render_bot_controls
from market.market_ui import render_market_feed
from market.crypto_prices import render_crypto_prices
render_crypto_prices()

def render_dashboard():
    st.markdown("##")
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    st.image(logo_path, width=80)

    st.markdown("<h2 style='color:#1E90FF;'>Elytrix Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-style: italic; color: #999;'>Precision Wins.</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital", "$5,200", "+4.2%")
    with col2:
        st.metric("Daily P/L", "+$210", "+1.3%")
    with col3:
        st.metric("Bot Status", "Running")

    st.markdown("---")
    render_bot_controls()
    st.markdown("---")
    render_market_feed()
