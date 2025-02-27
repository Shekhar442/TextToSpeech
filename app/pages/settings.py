import streamlit as st
from src.utils import clean_old_files

def render_settings_page():
    st.title("Settings ⚙️")

    st.subheader("File Management")

    # Clean old files
    col1, col2 = st.columns(2)
    
    with col1:
        days = st.number_input(
            "Delete files older than (days):",
            min_value=1,
            value=7
        )

        if st.button("Clean Old Files"):
            count, files = clean_old_files(days)
            if count > 0:
                st.success(f"Deleted {count} old files")
                if st.checkbox("Show deleted files"):
                    st.write(files)
            else:
                st.info("No files to clean")

    with col2:
        st.info("""
        File Management Tips:
        - Regular cleanup helps manage storage
        - Downloaded files are saved temporarily
        - Clean old files periodically
        """)

    # About section
    st.subheader("About")
    st.markdown("""
    Text to Speech Converter v1.0.0
    
    This application converts text to speech using Google's TTS service.
    Features:
    - Multiple language support
    - Adjustable speech rate
    - MP3 file download
    - Automatic file cleanup
    """)