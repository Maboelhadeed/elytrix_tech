
import streamlit as st
from dashboard import dashboard_ui, home_ui
from dashboard.config import DASHBOARD_CONFIG

st.set_page_config(
    page_title="Elytrix",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("dashboard/assets/elytrix_logo.png", "rb") as logo_file:
    st.sidebar.image(logo_file.read(), width=80)

st.sidebar.title("Elytrix Controls")
theme = st.sidebar.radio("Select Theme", ["Dark", "Light"])
page = st.sidebar.radio("Choose a tab", ["Home", "Dashboard"])

if page == "Home":
    home_ui.render_home()
elif page == "Dashboard":
    dashboard_ui.render_dashboard()
