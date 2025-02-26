import os

# Get the base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Voice settings configuration
VOICE_SETTINGS = {
    'rate': 150,          # Words per minute (default: 150)
    'volume': 1.0,        # Volume level 0.0 to 1.0 (default: 1.0)
    'voice_id': 0,        # Default voice ID
    'supported_rates': {
        'min': 50,        # Minimum speaking rate
        'max': 300,       # Maximum speaking rate
        'default': 150    # Default speaking rate
    },
    'supported_volumes': {
        'min': 0.0,       # Minimum volume
        'max': 1.0,       # Maximum volume
        'default': 1.0    # Default volume
    }
}

# Audio output configuration
AUDIO_OUTPUT = {
    'output_dir': os.path.join(BASE_DIR, 'audio_output'),
    'format': 'mp3',
    'supported_formats': ['mp3', 'wav'],
    'max_file_size_mb': 50,
    'cleanup_files_older_than_days': 7
}

# Application settings
APP_SETTINGS = {
    'app_name': 'Text to Speech Converter',
    'version': '1.0.0',
    'author': 'Your Name',
    'description': 'Convert text to speech with various voice options',
    'github_repo': 'https://github.com/yourusername/TextToSpeechProject'
}