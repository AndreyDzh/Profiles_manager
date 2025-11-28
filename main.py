
from src.cli.menus import main_menu, profile_list
from src.cli.cli_actions import cli_create_new_profile, cli_delete_profile, cli_open_profile

def main_loop():
    while True: 
        choice = main_menu()
        match choice:
            case "profile_list":
                profile_list_loop()
            case "create_new_profile":
                cli_create_new_profile()
            case "delete_profile":
                selected_profile = profile_list()
                if selected_profile != "back":
                    cli_delete_profile(selected_profile)
            case "exit":
                break

def profile_list_loop():
    while True:
        selected = profile_list()
        if selected == "back":

            return
        cli_open_profile(selected)

def main():
    main_loop()
    
if __name__ == "__main__":
    main()
