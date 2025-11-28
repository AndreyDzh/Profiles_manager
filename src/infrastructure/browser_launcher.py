import sys
import subprocess

from src.models.profiles import Profile 
from src.infrastructure.fs_profile_dir import get_profile_dir

def open_profile_in_browser(profile: Profile) -> None:
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