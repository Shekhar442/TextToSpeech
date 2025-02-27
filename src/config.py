import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# App configuration settings
APP_SETTINGS = {
    "app_name": "Text to Speech Converter",
    "version": "1.0.0",
    "output_dir": "./output",
    "temp_dir": "./temp",
    "max_text_length": 5000,
    "default_voice": "default",
    "supported_formats": ["mp3", "wav"],
    "default_format": "mp3"
}

# Voice settings
VOICE_SETTINGS = {
    'default_language': 'en',
    'default_slow': False
}

# Available languages
AVAILABLE_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'hi': 'Hindi',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ru': 'Russian'
}

# Audio output settings
AUDIO_OUTPUT = {
    'output_dir': os.path.join(BASE_DIR, 'audio_output'),
    'format': 'mp3',
    'cleanup_days': 7
}