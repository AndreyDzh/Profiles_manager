from questionary import select, Choice
from src.utils import profiles_load

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
    data_profiles = profiles_load()

    if not data_profiles:
        print("📭 No profiles found")
        return "back"
    
    profiles = [profile for profile in data_profiles]
    
    selected = select(
        message= "Select profile",
        choices= profiles + [Choice("Back", value= "back")],
        qmark= "⚙️",
        pointer= "✅"
    ).ask()
    return selected