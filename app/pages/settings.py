import streamlit as st
from src.utils import clear_audio_files
from src.config import AUDIO_OUTPUT, APP_SETTINGS

def render_settings_page():
    """Render the settings page"""
    st.title("Settings ⚙️")
    
    # Application Information
    st.subheader("Application Information")
    st.info(
        f"**{APP_SETTINGS['app_name']}** v{APP_SETTINGS['version']}\n\n"
        f"{APP_SETTINGS['description']}\n\n"
        f"Created by: {APP_SETTINGS['author']}"
    )
    
    # Audio Settings
    st.subheader("Audio Settings")
    st.write("Current audio output directory:", AUDIO_OUTPUT['output_dir'])
    st.write("Supported audio formats:", ", ".join(AUDIO_OUTPUT['supported_formats']))
    
    # File Management
    st.subheader("File Management")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear All Audio Files"):
            try:
                files_deleted, deleted_list = clear_audio_files()
                if files_deleted > 0:
                    st.success(f"Cleared {files_deleted} audio files!")
                    if st.checkbox("Show deleted files"):
                        st.write(deleted_list)
                else:
                    st.info("No audio files to clear.")
            except Exception as e:
                st.error(f"Error clearing files: {str(e)}")
    
    with col2:
        days = st.number_input(
            "Clear files older than (days):",
            min_value=1,
            value=7
        )
        if st.button("Clear Old Files"):
            try:
                files_deleted, deleted_list = clear_audio_files(days_old=days)
                if files_deleted > 0:
                    st.success(f"Cleared {files_deleted} files older than {days} days!")
                    if st.checkbox("Show deleted files"):
                        st.write(deleted_list)
                else:
                    st.info("No old files to clear.")
            except Exception as e:
                st.error(f"Error clearing files: {str(e)}")
    
    # Current Engine Settings
    st.subheader("Current Engine Settings")
    current_settings = st.session_state.tts_engine.get_current_settings()
    st.json(current_settings)