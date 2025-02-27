from gtts import gTTS
import os
from datetime import datetime
from typing import Optional
from .config import VOICE_SETTINGS, AUDIO_OUTPUT, AVAILABLE_LANGUAGES

class TTSEngine:
    def __init__(self):
        """Initialize TTS engine and ensure output directory exists"""
        self._ensure_output_directory()

    def _ensure_output_directory(self) -> None:
        """Create output directory if it doesn't exist"""
        os.makedirs(AUDIO_OUTPUT['output_dir'], exist_ok=True)

    def convert_to_speech(self, 
                         text: str, 
                         language: str = 'en',
                         slow: bool = False) -> str:
        """
        Convert text to speech and save as audio file
        
        Args:
            text: Text to convert
            language: Language code (e.g., 'en', 'es')
            slow: Whether to speak slowly
            
        Returns:
            Path to the generated audio file
        """
        if not text.strip():
            raise ValueError("Text cannot be empty")

        try:
            # Create TTS object
            tts = gTTS(text=text, lang=language, slow=slow)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"speech_{timestamp}.mp3"
            filepath = os.path.join(AUDIO_OUTPUT['output_dir'], filename)
            
            # Save to file
            tts.save(filepath)
            
            return filepath
        except Exception as e:
            raise Exception(f"TTS conversion failed: {str(e)}")

    def get_available_languages(self) -> dict:
        """Get dictionary of available languages"""
        return AVAILABLE_LANGUAGES