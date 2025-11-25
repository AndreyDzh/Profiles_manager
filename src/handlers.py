import os, sys
import subprocess

from pathlib import Path
from questionary import text, confirm
from src.utils import profiles_load, profiles_dump
from config import DATA_DIR, HOMEPAGE_DEFAULT, PROXY_DEFAULT, WINDOWS_CHROME_PATH

def profile_open(profile):
    data = profiles_load()
    p = data[profile]

    dir_to_profile = Path(DATA_DIR) / "profiles_data" / profile
    proxy = p["proxy"]
    homepage = p["homepage"]

    flags = [
        f'--user-data-dir={dir_to_profile}',
        '--profile-directory=Default',
        f'--proxy-server={proxy}',
        homepage,
    ]

    if sys.platform == "darwin":
        subprocess.Popen(["open", "-na", "Google Chrome", "--args", *flags])
    else:  # Windows
        subprocess.Popen([WINDOWS_CHROME_PATH, *flags])

def create_new_profile():
    data = profiles_load()
    print("‼️ For cancel leave the next field empty ‼️")
    profile_name = text("Profile name:", qmark= "⏩").ask().strip()
    if not profile_name or profile_name in data:
        print("📛 CANCELED 📛")
        return
    
    proxy = text("Proxy:", qmark="⏩").ask() or PROXY_DEFAULT
    homepage = text("Homepage:", qmark="⏩").ask() or HOMEPAGE_DEFAULT

    data[profile_name] = {
        "proxy": proxy,
        "homepage": homepage
    }
    profiles_dump(data)
    print("✅ PROFILE ADDED ✅")

    
def delete_profile(profile):
    data = profiles_load()
    confirm_status = confirm("Are you sure?", qmark= "⁉️").ask()
    if not confirm_status:
        print("📛 CANCELED 📛")
        return
    
    data.pop(profile)

    dir_to_profile = Path(DATA_DIR) / "profiles_data" / profile

    if os.path.isdir(dir_to_profile):
        if sys.platform == "darwin":
            subprocess.run(["rm", "-rf", dir_to_profile], check=False)
        else:
            subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", dir_to_profile], check=False)

    print("✅ PROFILE DELETED ✅")
    profiles_dump(data)
