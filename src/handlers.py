import os
import subprocess

from questionary import text, confirm
from src.utils import profiles_load, profiles_dump
from config import DATA_DIR, HOMEPAGE_DEFAULT, PROXY_DEFAULT

def profile_open(profile):
    data = profiles_load()
    profile_data = data[profile]
    
    dir_to_profile = os.path.join(DATA_DIR, profile)

    proxy = profile_data["proxy"]
    homepage = profile_data["homepage"]

    args = [
        "open", "-na", "Google Chrome", "--args",
        f'--user-data-dir={dir_to_profile}',
        '--profile-directory=Default',
        f'--proxy-server={proxy}',
        homepage,
    ]

    subprocess.Popen(args)

def create_new_profile():
    data = profiles_load()
    print("\033[1m‼️ For cancel leave the next field empty ‼️")
    profile_name = text("Profile name:", qmark= "⏩").ask().strip()
    if not profile_name or profile_name in data:
        print("\033[1m📛 CANCELED 📛")
        return
    
    proxy = text("Proxy:", qmark="⏩").ask() or PROXY_DEFAULT
    homepage = text("Homepage:", qmark="⏩").ask() or HOMEPAGE_DEFAULT

    data[profile_name] = {
        "proxy": proxy,
        "homepage": homepage
    }
    profiles_dump(data)
    print("\033[1m✅ PROFILE ADDED ✅")

    
def delete_profile(profile):
    data = profiles_load()
    confirm_status = confirm("Are you sure?", qmark= "⁉️").ask()
    if not confirm_status:
        print("\033[1m📛 CANCELED 📛")
        return
    
    data.pop(profile)

    dir_to_profile = os.path.join(DATA_DIR, profile)

    if os.path.isdir(dir_to_profile):
        subprocess.run(["rm", "-rf", dir_to_profile], check=False)

    print("\033[1m✅ PROFILE DELETED ✅")
    profiles_dump(data)
