from questionary import text, confirm

from src.cli.helpers import is_text_empty
from src.services.profile_service import ProfileService


service = ProfileService()

def cli_create_new_profile():
    name = text("Profile name:", qmark="⏩").ask() 

    if is_text_empty(name):
        return 
    
    proxy = text("Proxy:", qmark="⏩").ask()
    homepage = text("Homepage:", qmark="⏩").ask()

    try:
        service.create_profile(name, proxy, homepage)
        print("✅ PROFILE ADDED ✅")
    except ValueError as e:
        print(f"📛 {e} 📛")

def cli_delete_profile(profile):

    ok = confirm("Are you sure?", qmark="⁉️").ask()

    if not ok:
        print("❎ PROFILE NOT DELETED ❎")
        return

    try:
        service.delete_profile(profile)
        print("✅ PROFILE DELETED ✅")
    except ValueError as e:
        print(f"📛 {e} 📛")

def cli_open_profile(profile):
    service.open_profile(profile)

def _cli_change_field(profile, label: str, field: str):
    print(f"🔰 TYPE 'DEFAULT' TO SET THE DEFAULT {label} 🔰")
    new_value = text(f"New {label.lower()}:", qmark="⏩").ask()

    if is_text_empty(new_value):
        return 

    try:
        profile = service.update_profile(profile, field, new_value)
        print(f"✅ {label} CHANGED ✅")
        return profile
    except ValueError as e:
        print(f"📛 {e} 📛")

def cli_change_name(profile):
    return _cli_change_field(
        profile=profile,
        label="NAME",
        field="name",
    )

def cli_change_proxy(profile):
    return _cli_change_field(
        profile=profile,
        label="PROXY",
        field="proxy",
    )


def cli_change_homepage(profile):
    return _cli_change_field(
        profile=profile,
        label="HOMEPAGE",
        field="homepage",
    )
