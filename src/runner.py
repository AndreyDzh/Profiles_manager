from src.cli.menus import (
    main_menu, 
    profile_list, 
    profile_menu
)

from src.cli.cli_actions import (
    cli_create_new_profile,
    cli_delete_profile,
    cli_open_profile,
    cli_change_proxy,
    cli_change_homepage,
    cli_change_name
)

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
        profile_menu_loop(selected)

def profile_menu_loop(selected):
    while True:
        choice = profile_menu(selected)
        match choice:
            case "open_profile":
                cli_open_profile(selected)
            
            case "change_name":
                updated = cli_change_name(selected)
                if updated is not None:
                    selected = updated

            case "change_proxy":
                updated = cli_change_proxy(selected)
                if updated is not None:
                    selected = updated

            case "change_homepage":
                updated = cli_change_homepage(selected)
                if updated is not None:
                    selected = updated
            case "back":
                break

def run_cli():
    main_loop()
