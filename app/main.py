import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import APP_SETTINGS
from src.tts_engine import TTSEngine
from components.sidebar import render_sidebar
from pages.text_to_speech import render_text_to_speech_page
from pages.settings import render_settings_page

def initialize_session_state():
    """Initialize session state variables"""
    if 'tts_engine' not in st.session_state:
        st.session_state.tts_engine = TTSEngine()
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Text to Speech"

def main():
    # Configure the Streamlit page
    st.set_page_config(
        page_title=APP_SETTINGS['app_name'],
        page_icon="🔊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize session state
    initialize_session_state()

    # Render sidebar and get selected page
    selected_page = render_sidebar()

    # Render the selected page
    if selected_page == "Text to Speech":
        render_text_to_speech_page()
    elif selected_page == "Settings":
        render_settings_page()

    # Add footer
    st.markdown("---")
    st.markdown(
        f"<div style='text-align: center'>{APP_SETTINGS['app_name']} v{APP_SETTINGS['version']} | "
        f"Created by {APP_SETTINGS['author']}</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()