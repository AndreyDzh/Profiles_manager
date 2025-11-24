# Chrome Profiles Proxy Manager

## Project Purpose
This project manages multiple Google Chrome profiles that use proxies.  
Profiles are launched from the terminal via command line.

## Important Notes
- The app works **only** with proxies in **login:password** format.
- On the **first run of a profile**, you must enter the proxy login and password manually.
- After that, **save them in Chrome’s Password Manager** so future launches can authenticate automatically.

---

## PROGRAM — FIRST RUN

1. Open the project folder.  
2. Create a virtual environment inside it:
   ```bash
   python3 -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
4. Install the requirements:
   ```bash
   pip3 install -r requirements.txt
   ```
5. Run `main.py`:
   ```bash
   python3 main.py
   ```

---

## PROGRAM — SECOND RUN

1. Open the project folder.  
2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
3. Run `main.py`:
   ```bash
   python3 main.py
   ```

---

## PROFILE — FIRST RUN

1. Enter the proxy login and password in the Chrome pop‑up/fields.  
2. Save them in Chrome’s password manager.
