import pyttsx3
import comtypes
import os
from datetime import datetime
from typing import Tuple, List, Optional
from .config import VOICE_SETTINGS, AUDIO_OUTPUT

class TTSEngine:
    """
    Text-to-Speech Engine class that handles all TTS operations
    """
    
    def __init__(self):
         # Initialize COM before creating the pyttsx3 engine
        comtypes.CoInitialize()
        self.engine = pyttsx3.init()
        """Initialize the TTS engine with default settings"""
        self.engine = pyttsx3.init()
        self.output_dir = AUDIO_OUTPUT['output_dir']
        self._configure_engine()
        self._ensure_output_directory()
        
    def _configure_engine(self) -> None:
        """Configure the TTS engine with default settings"""
        self.engine.setProperty('rate', VOICE_SETTINGS['rate'])
        self.engine.setProperty('volume', VOICE_SETTINGS['volume'])
        
        # Set default voice
        voices = self.engine.getProperty('voices')
        if voices and len(voices) > VOICE_SETTINGS['voice_id']:
            self.engine.setProperty('voice', voices[VOICE_SETTINGS['voice_id']].id)
    
    def _ensure_output_directory(self) -> None:
        """Ensure the output directory exists"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_available_voices(self) -> List[Tuple[int, str]]:
        """
        Get list of available voices
        
        Returns:
            List of tuples containing voice ID and name
        """
        voices = self.engine.getProperty('voices')
        return [(idx, voice.name) for idx, voice in enumerate(voices)]
    
    def save_to_file(self, text: str, filename: Optional[str] = None) -> str:
        """
        Convert text to speech and save to file
        
        Args:
            text: Text to convert to speech
            filename: Optional filename, generates timestamp-based name if None
            
        Returns:
            Path to the saved audio file
            
        Raises:
            Exception: If there's an error during file saving
        """
        if not text.strip():
            raise ValueError("Text cannot be empty")
            
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"speech_{timestamp}.{AUDIO_OUTPUT['format']}"
            
        try:
            file_path = os.path.join(self.output_dir, filename)
            self.engine.save_to_file(text, file_path)
            self.engine.runAndWait()
            return file_path
        except Exception as e:
            raise Exception(f"Error saving audio file: {str(e)}")
    
    def update_settings(self, 
                       rate: Optional[int] = None, 
                       volume: Optional[float] = None, 
                       voice_id: Optional[int] = None) -> bool:
        """
        Update TTS engine settings
        
        Args:
            rate: Speaking rate (words per minute)
            volume: Volume level (0.0 to 1.0)
            voice_id: Voice ID to use
            
        Returns:
            bool: True if settings were updated successfully
        """
        try:
            if rate is not None:
                if VOICE_SETTINGS['supported_rates']['min'] <= rate <= VOICE_SETTINGS['supported_rates']['max']:
                    self.engine.setProperty('rate', rate)
                else:
                    raise ValueError(f"Rate must be between "
                                   f"{VOICE_SETTINGS['supported_rates']['min']} and "
                                   f"{VOICE_SETTINGS['supported_rates']['max']}")
            
            if volume is not None:
                if 0.0 <= volume <= 1.0:
                    self.engine.setProperty('volume', volume)
                else:
                    raise ValueError("Volume must be between 0.0 and 1.0")
            
            if voice_id is not None:
                voices = self.engine.getProperty('voices')
                if voice_id < len(voices):
                    self.engine.setProperty('voice', voices[voice_id].id)
                else:
                    raise ValueError(f"Voice ID {voice_id} not available")
                    
            return True
            
        except Exception as e:
            print(f"Error updating settings: {str(e)}")
            return False
    
    def get_current_settings(self) -> dict:
        """
        Get current TTS engine settings
        
        Returns:
            Dictionary containing current settings
        """
        return {
            'rate': self.engine.getProperty('rate'),
            'volume': self.engine.getProperty('volume'),
            'voice_id': VOICE_SETTINGS['voice_id'],
            'output_format': AUDIO_OUTPUT['format']
        }