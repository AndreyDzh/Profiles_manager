
import sys
import subprocess
from pathlib import Path
from typing import List

from questionary import text, confirm

from config import DATA_DIR, HOMEPAGE_DEFAULT, PROXY_DEFAULT, WINDOWS_CHROME_PATH
from src.profiles import Profile
from src.utils import profiles_load, profiles_dump

PROFILE_DATA_DIR = Path(DATA_DIR) / "profiles_data"


def get_profile_dir(profile: Profile) -> Path:
    return PROFILE_DATA_DIR / profile.name


def profile_open(profile: Profile) -> None:
    dir_to_profile = get_profile_dir(profile)

    flags = [
        f"--user-data-dir={dir_to_profile}",
        "--profile-directory=Default",
        f"--proxy-server={profile.proxy}",
        profile.homepage,
    ]

    if sys.platform == "darwin":
        subprocess.Popen(["open", "-na", "Google Chrome", "--args", *flags])
    else:  # Windows
        subprocess.Popen([WINDOWS_CHROME_PATH, *flags])


def create_new_profile() -> None:
    data: List[Profile] = profiles_load()
    print("‼️ For cancel leave the next field empty ‼️")

    answer = text("Profile name:", qmark="⏩").ask()
    if not answer:
        print("📛 CANCELED 📛")
        return

    profile_name = answer.strip()
    if not profile_name:
        print("📛 CANCELED 📛")
        return

    if any(p.name.lower() == profile_name.lower() for p in data):
        print("📛 PROFILE WITH THIS NAME ALREADY EXIST 📛")
        return

    proxy = text("Proxy:", qmark="⏩").ask() or PROXY_DEFAULT
    homepage = text("Homepage:", qmark="⏩").ask() or HOMEPAGE_DEFAULT

    new_profile = Profile(profile_name, proxy, homepage)
    data.append(new_profile)

    profiles_dump(data)
    print("✅ PROFILE ADDED ✅")


def delete_profile(profile: Profile) -> None:
    data: List[Profile] = profiles_load()

    confirm_status = confirm("Are you sure?", qmark="⁉️").ask()
    if not confirm_status:
        print("📛 CANCELED 📛")
        return

    # прибираємо профіль зі списку
    data = [p for p in data if p.name != profile.name]

    dir_to_profile = get_profile_dir(profile)

    if dir_to_profile.is_dir():
        if sys.platform == "darwin":
            subprocess.run(["rm", "-rf", str(dir_to_profile)], check=False)
        else:
            subprocess.run(
                ["cmd", "/c", "rmdir", "/s", "/q", str(dir_to_profile)],
                check=False,
            )

    profiles_dump(data)
    print("✅ PROFILE DELETED ✅")
