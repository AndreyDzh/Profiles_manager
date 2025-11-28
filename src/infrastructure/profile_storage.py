import json
from pathlib import Path

from src.models.profiles import Profile
from config import FOLDER_PATH, DATA_DIR_NAME, JSON_FILE_NAME

path = Path(FOLDER_PATH) / DATA_DIR_NAME / JSON_FILE_NAME

def profiles_load():
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        save_profiles([])
        return []
    
    with path.open("r", encoding= "utf-8") as f:
        raw_dict = json.load(f)
        profiles = [Profile.from_dict(item) for item in raw_dict]
        return profiles
        
def save_profiles(data):
    processed_data = [item.to_dict() for item in data]
     
    with path.open("w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)