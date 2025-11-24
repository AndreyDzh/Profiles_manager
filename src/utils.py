import json
from config import DATA_DIR
from pathlib import Path

CONFIG_PATH = Path(DATA_DIR) / "profiles.json"

def create_json_file():
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps({}, indent=2))

def profiles_load():
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    else:
        create_json_file()
        return {}
        
def profiles_dump(data):
    CONFIG_PATH.write_text(json.dumps(data, indent=2))