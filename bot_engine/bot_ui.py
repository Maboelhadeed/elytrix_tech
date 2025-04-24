
import streamlit as st
import random

def render_bot_controls():
    st.subheader("Bot Control Panel")

    strategy = st.selectbox("Select Strategy", ["AI Adaptive", "Scalping", "Sniper"])
    run_bot = st.button("Run Bot")
    stop_bot = st.button("Stop Bot")

    st.markdown("### Bot Logs")
    if run_bot:
        st.success(f"{strategy} strategy started.")
        for i in range(3):
            st.text(f"[INFO] {strategy} executed trade #{random.randint(1000, 9999)}")
    elif stop_bot:
        st.warning("Bot stopped.")

