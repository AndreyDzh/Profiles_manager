from src.models.profiles import Profile
from src.infrastructure.profile_storage import profiles_load, save_profiles
from src.infrastructure.browser_launcher import open_profile_in_browser
from src.infrastructure.fs_profile_dir import remove_profile_dir
from config import HOMEPAGE_DEFAULT, PROXY_DEFAULT

class ProfileService: 

    def get_profile_list(self):
        return profiles_load()

    def open(self, profile: Profile) -> None: 
        open_profile_in_browser(profile)
    
    def create(self, name, proxy, homepage) -> Profile:
        
        if not name:
            raise ValueError("Empty name")

        profiles = profiles_load()

        if any(profile.name.lower() == name.lower() for profile in profiles):
            raise ValueError("Profile with this name already exist")

        profile = Profile(
            name.strip(),
            proxy or PROXY_DEFAULT ,
            homepage or HOMEPAGE_DEFAULT
        )

        profiles.append(profile)
        save_profiles(profiles)

    def delete(self, profile: Profile) -> None:
        profiles = profiles_load()
        profiles = [p for p in profiles if p.name != profile.name]
        save_profiles(profiles)
        remove_profile_dir(profile)
        