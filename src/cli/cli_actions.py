from questionary import text, confirm

from src.services.profile_service import ProfileService


service = ProfileService()

def cli_create_new_profile():
    print("‼️ For cancel leave the next field empty ‼️")
    name = text("Profile name:", qmark="⏩").ask() 

    if not name:
        print("📛 CANCELED 📛")
        return    
    
    proxy = text("Proxy:", qmark="⏩").ask()
    homepage = text("Homepage:", qmark="⏩").ask()

    try:
        service.create(name, proxy, homepage)
        print("✅ PROFILE ADDED ✅")
    except ValueError as e:
        print(f"📛 {e} 📛")

def cli_delete_profile(profile):

    ok = confirm("Are you sure?", qmark="⁉️").ask()
    if not ok:
        print("📛 CANCELED 📛")
        return

    try:
        service.delete(profile)
        print("✅ PROFILE DELETED ✅")
    except ValueError as e:
        print(f"📛 {e} 📛")

def cli_open_profile(profile):
    service.open(profile)