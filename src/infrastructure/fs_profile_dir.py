import sys
import subprocess

from pathlib import Path

from config import FOLDER_PATH, DATA_DIR_NAME
from src.models.profiles import Profile


PROFILE_DATA_DIR = Path(FOLDER_PATH) / DATA_DIR_NAME

def get_profile_dir(profile: Profile) -> Path:
    return PROFILE_DATA_DIR / profile.name

def remove_profile_dir(profile: Profile) -> None:
    dir_to_profile = get_profile_dir(profile)

    if dir_to_profile.is_dir():
        if sys.platform == "darwin":
            subprocess.run(["rm", "-rf", str(dir_to_profile)], check=False)
        else:
            subprocess.run(
                ["cmd", "/c", "rmdir", "/s", "/q", str(dir_to_profile)],
                check=False,
            )

