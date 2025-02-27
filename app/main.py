'''
import streamlit as st
from pages.text_to_speech import render_text_to_speech_page
from pages.settings import render_settings_page
from components.sidebar import render_sidebar

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
'''
import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pages.text_to_speech import render_text_to_speech_page
from pages.settings import render_settings_page
from components.sidebar import render_sidebar

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