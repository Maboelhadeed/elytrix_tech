
import streamlit as st

def render_home():
    st.image("dashboard/assets/elytrix_logo.png", width=150)
    st.title("Welcome to Elytrix")
    st.markdown("*Precision Wins.*")
    if st.button("Launch Dashboard"):
        st.experimental_set_query_params(page="Dashboard")
