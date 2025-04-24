
import streamlit as st
import os

def render_home():
    st.markdown("##")
    logo_path = os.path.join("dashboard", "assets", "elytrix_logo.png")
    st.image(logo_path, width=180)

    st.markdown("<h1 style='text-align:center; color:#1E90FF;'>Welcome to Elytrix</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-style: italic;'>Precision Wins.</p>", unsafe_allow_html=True)
    st.markdown("##")

    centered_button = '''
    <div style="text-align:center;">
        <a href="?page=Dashboard">
            <button style="padding:10px 30px; font-size:16px; background-color:#1E90FF; color:white; border:none; border-radius:6px; cursor:pointer;">
                Launch Dashboard
            </button>
        </a>
    </div>
    '''
    st.markdown(centered_button, unsafe_allow_html=True)
