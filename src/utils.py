import json
from config import DATA_DIR
from pathlib import Path

PATH = Path(DATA_DIR) / "profiles.json"

def create_json_file():
    PATH.parent.mkdir(parents=True, exist_ok=True)
    PATH.write_text(json.dumps({}, indent=2))

def profiles_load():
    if PATH.exists():
        return json.loads(PATH.read_text())
    else:
        create_json_file()
        return {}
        
def profiles_dump(data):
    PATH.write_text(json.dumps(data, indent=2))