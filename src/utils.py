import json
from pathlib import Path

from src.profiles import Profile
from config import DATA_DIR

path = Path(DATA_DIR) / "profiles_data" / "profiles.json"

def profiles_load():
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        profiles_dump([])
        return []
    
    with path.open("r", encoding= "utf-8") as f:
        raw_dict = json.load(f)
        profiles = [Profile.from_dict(item) for item in raw_dict]
        return profiles
        
def profiles_dump(data):
    processed_data = [item.to_dict() for item in data]
     
    with path.open("w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)