from questionary import select, Choice
from src.infrastructure.profile_storage import profiles_load
from src.services.profile_service import ProfileService

service = ProfileService()

def main_menu():
    selected = select(
        message= "Main menu",
        choices= [
            Choice("Profile list", value= "profile_list"),
            Choice("Create new profile", value= "create_new_profile"),
            Choice("Delete profile", value= "delete_profile"),
            Choice("Exit", value= "exit")
        ],
        qmark= "⚙️",
        pointer= "✅"
    ).ask()
    return selected

def profile_list():
    profiles = service.get_profile_list() 
    if not profiles:
        print("📭 No profiles found")
        return "back"
    
    profiles_to_choice = [
        Choice(title=profile.name, value=profile)
        for profile in profiles
    ]
    profiles_to_choice.append(Choice("Back", value="back"))

    selected = select(
        message="Select profile",
        choices=profiles_to_choice,
        qmark="⚙️",
        pointer="✅"
    ).ask()
    return selected

def profile_menu(profile):
    selected = select(
        message= f"SELECTED {profile.name}",
        choices= [
            Choice("Open", value= "open_profile"),
            Choice(f"Change name({profile.name})", value= "change_name"),
            Choice(f"Change proxy({profile.proxy})", value= "change_proxy"),
            Choice(f"Change homepage({profile.homepage})", value= "change_homepage"),
            Choice("Back", value= "back")
        ],
        qmark= "⚙️",
        pointer= "✅"
    ).ask()
    return selected