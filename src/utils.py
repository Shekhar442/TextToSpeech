import os
import base64
from datetime import datetime, timedelta
from typing import Optional
from typing import Tuple, Optional
from .config import AUDIO_OUTPUT

def get_binary_file_downloader_html(bin_file: str, file_label: str = 'File') -> str:
    """
    Generate HTML for file download link
    
    Args:
        bin_file: Path to the binary file
        file_label: Label for the download link
        
    Returns:
        HTML string for file download
    """
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" ' \
               f'download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
    except Exception as e:
        return f"Error generating download link: {str(e)}"

def clear_audio_files(directory: Optional[str] = None, 
                     days_old: Optional[int] = None) -> Tuple[int, list]:
    """
    Clear audio files from the specified directory
    
    Args:
        directory: Directory to clear files from (default: AUDIO_OUTPUT['output_dir'])
        days_old: Only clear files older than this many days
        
    Returns:
        Tuple containing count of files deleted and list of deleted files
    """
    if directory is None:
        directory = AUDIO_OUTPUT['output_dir']
        
    if not os.path.exists(directory):
        return 0, []
        
    deleted_files = []
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip if not an audio file
        if not file.endswith(tuple(AUDIO_OUTPUT['supported_formats'])):
            continue
            
        # Check file age if days_old is specified
        if days_old is not None:
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if datetime.now() - file_time < timedelta(days=days_old):
                continue
                
        try:
            os.remove(file_path)
            deleted_files.append(file)
        except Exception as e:
            print(f"Error deleting {file}: {str(e)}")
            
    return len(deleted_files), deleted_files

def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in megabytes
    
    Args:
        file_path: Path to the file
        
    Returns:
        File size in megabytes
    """
    return os.path.getsize(file_path) / (1024 * 1024)

def is_valid_audio_file(file_path: str) -> bool:
    """
    Check if file is a valid audio file
    
    Args:
        file_path: Path to the file
        
    Returns:
        bool: True if file is valid
    """
    # Check file extension
    if not file_path.endswith(tuple(AUDIO_OUTPUT['supported_formats'])):
        return False
        
    # Check file size
    if get_file_size_mb(file_path) > AUDIO_OUTPUT['max_file_size_mb']:
        return False
        
    return True