import streamlit as st
from src.utils import get_binary_file_downloader_html

def render_text_to_speech_page():
    """Render the text-to-speech conversion page"""
    st.title("Text to Speech Converter 🎧")
    
    # Create two columns for the layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Text input area
        text_input = st.text_area(
            "Enter your text here:",
            height=200,
            placeholder="Type or paste your text here..."
        )
        
        # Generate button
        if st.button("Generate Audio", type="primary"):
            if text_input.strip():
                try:
                    with st.spinner("Generating audio..."):
                        audio_file = st.session_state.tts_engine.save_to_file(text_input)
                        st.success("Audio generated successfully!")
                        
                        # Display audio player
                        st.audio(audio_file)
                        
                        # Display download button
                        st.markdown(
                            get_binary_file_downloader_html(audio_file, 'Audio'),
                            unsafe_allow_html=True
                        )
                except Exception as e:
                    st.error(f"Error generating audio: {str(e)}")
            else:
                st.warning("Please enter some text first!")
    
    with col2:
        st.subheader("Voice Settings")
        
        # Voice selection
        voices = st.session_state.tts_engine.get_available_voices()
        voice_options = {voice[1]: voice[0] for voice in voices}
        selected_voice = st.selectbox(
            "Select Voice:",
            list(voice_options.keys())
        )
        
        # Speech rate slider
        rate = st.slider(
            "Speech Rate:",
            min_value=50,
            max_value=300,
            value=150,
            help="Adjust the speaking speed (words per minute)"
        )
        
        # Volume slider
        volume = st.slider(
            "Volume:",
            min_value=0.0,
            max_value=1.0,
            value=1.0,
            step=0.1,
            help="Adjust the volume level"
        )
        
        # Apply settings button
        if st.button("Apply Settings"):
            try:
                st.session_state.tts_engine.update_settings(
                    rate=rate,
                    volume=volume,
                    voice_id=voice_options[selected_voice]
                )
                st.success("Settings updated successfully!")
            except Exception as e:
                st.error(f"Error updating settings: {str(e)}")