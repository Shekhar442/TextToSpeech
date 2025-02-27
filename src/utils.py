import os
from datetime import datetime, timedelta
from typing import Tuple, List
from .config import AUDIO_OUTPUT

def clean_old_files(days: int = 7) -> Tuple[int, List[str]]:
    """
    Delete audio files older than specified days
    
    Args:
        days: Number of days old to clean
        
    Returns:
        Tuple of (number of files deleted, list of deleted files)
    """
    deleted_files = []
    directory = AUDIO_OUTPUT['output_dir']
    
    if not os.path.exists(directory):
        return 0, []
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    for filename in os.listdir(directory):
        if not filename.endswith('.mp3'):
            continue
            
        file_path = os.path.join(directory, filename)
        file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        if file_modified < cutoff_date:
            try:
                os.remove(file_path)
                deleted_files.append(filename)
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
    
    return len(deleted_files), deleted_files