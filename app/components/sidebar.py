import streamlit as st
from src.config import APP_SETTINGS

def render_sidebar():
    """Render the sidebar navigation"""
    with st.sidebar:
        st.title("Navigation 🧭")
        
        # Navigation selection
        selected_page = st.radio(
            "Go to:",
            ["Text to Speech", "Settings"]
        )
        
        st.markdown("---")
        
        # About section
        st.markdown("### About")
        st.info(
            f"Welcome to {APP_SETTINGS['app_name']}! "
            "This application allows you to convert text to speech "
            "using various voices and settings."
        )
        
        # GitHub link
        if APP_SETTINGS['github_repo']:
            st.markdown("### Links")
            st.markdown(f"[GitHub Repository]({APP_SETTINGS['github_repo']})")
        
        # Additional information
        st.markdown("### Help")
        with st.expander("How to use"):
            st.markdown("""
                1. Go to 'Text to Speech' page
                2. Enter or paste your text
                3. Adjust voice settings if needed
                4. Click 'Generate Audio'
                5. Play or download the generated audio
            """)
    
    return selected_page