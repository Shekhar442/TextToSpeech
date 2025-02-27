import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Local imports
from app.pages.text_to_speech import render_text_to_speech_page
from app.pages.settings import render_settings_page
from app.components.sidebar import render_sidebar

def main():
    st.set_page_config(
        page_title="Text to Speech Converter",
        page_icon="🎙️",
        layout="wide"
    )

    # Render sidebar and get selected page
    selected_page = render_sidebar()

    # Render selected page
    if selected_page == "Text to Speech":
        render_text_to_speech_page()
    elif selected_page == "Settings":
        render_settings_page()

if __name__ == "__main__":
    main()