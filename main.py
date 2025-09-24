import os
import sys
import requests
import getpass

running = True
pltform = sys.platform

CONFIG_DIR = os.path.expanduser("~/.config/clue")
os.makedirs(CONFIG_DIR, exist_ok=True)
USER_INFO_FILE = os.path.join(CONFIG_DIR, "info.txt")

if os.path.exists(USER_INFO_FILE):
    with open(USER_INFO_FILE, "r", encoding="utf-8") as f:
        username_for_path = f.read().strip()
else:
    username_for_path = getpass.getuser()
    with open(USER_INFO_FILE, "w", encoding="utf-8") as f:
        f.write(username_for_path)

DOC_DIR = os.path.expanduser(f"/home/{username_for_path}/clue_docs")
os.makedirs(DOC_DIR, exist_ok=True)
DOC_FILE = os.path.join(DOC_DIR, "doc.txt")


def clear_console():
    if pltform == "linux":
        os.system("clear")
    elif pltform == "win32":
        os.system("cls")


while running:
    if pltform == "win32":
        print("This program only runs on Linux")
        break

    clear_console()
    command = input("Enter the command you want to know about [quit to exit]: ").lower()

    DOC_FILE = os.path.join(DOC_DIR, f"{command}_doc.txt")

    if not os.path.exists(DOC_FILE):
        with open(DOC_FILE, "w", encoding="utf-8") as f:
            f.write("# Command Documentation\n\n")

    if command == "quit":
        print("Goodbye!")
        break

    def receive_info_command(cmd):
        url = f"https://cheat.sh/{cmd}?QT"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(DOC_FILE, "a", encoding="utf-8") as f:
                    f.write(
                        f"\n-----------------------------\n"
                        f"Command: {cmd}\n"
                        f"-----------------------------\n"
                        f"{response.text}\n"
                        f"-----------------------------\n"
                    )
                clear_console()
                os.system(f"bat --pager='less -R +1' --style=plain {DOC_FILE}")
            else:
                print("Error fetching cheat sheet.")
        except Exception as e:
            print(f"Request failed: {e}")

    receive_info_command(command)

    choice = input("Do you want to try the command (y/n): ").lower()
    if choice == "y":
        params = input("Enter any parameters (or press Enter to skip): ")
        full_command = f"{command} {params}".strip()
        os.system(full_command)
    else:
        print("Okay, not running the command.")

    input("Press Enter to continue...")
    clear_console()
