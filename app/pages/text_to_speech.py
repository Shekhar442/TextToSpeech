import streamlit as st
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.tts_engine import TTSEngine

def render_text_to_speech_page():
    st.title("Text to Speech Converter 🎙️")

    # Initialize TTS engine if not in session state
    if 'tts_engine' not in st.session_state:
        st.session_state.tts_engine = TTSEngine()

    # Get available languages
    languages = st.session_state.tts_engine.get_available_languages()

    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Text input
        text_input = st.text_area(
            "Enter your text:",
            height=200,
            placeholder="Type or paste your text here..."
        )

        if st.button("Convert to Speech", type="primary"):
            if text_input.strip():
                try:
                    with st.spinner("Converting text to speech..."):
                        audio_file = st.session_state.tts_engine.convert_to_speech(
                            text=text_input,
                            language=st.session_state.get('language', 'en'),
                            slow=st.session_state.get('slow', False)
                        )

                        # Display audio player
                        st.audio(audio_file)

                        # Download button
                        with open(audio_file, 'rb') as f:
                            st.download_button(
                                "Download Audio",
                                f,
                                file_name=os.path.basename(audio_file),
                                mime="audio/mp3"
                            )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text first!")

    with col2:
        st.subheader("Voice Settings")

        # Language selection
        selected_language = st.selectbox(
            "Language:",
            options=list(languages.keys()),
            format_func=lambda x: languages[x]
        )
        st.session_state.language = selected_language

        # Speech rate
        slow_speech = st.checkbox("Slow speech rate")
        st.session_state.slow = slow_speech

        # Display current settings
        st.info(f"""
        Current Settings:
        - Language: {languages[selected_language]}
        - Speech Rate: {'Slow' if slow_speech else 'Normal'}
        """)