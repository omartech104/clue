import os, sys, requests
from colorama import init, Fore, Style

init(autoreset=True)

running=True
pltform = sys.platform

while running:
    if pltform == "linux":
        running=True
        os.system("clear")
    elif pltform == "win32":
        running=False
        print("This program only runs on Linux")
    else:
        running=False
        print("This program only runs on Linux")
    
    command = input(Fore.CYAN + Style.BRIGHT + "Enter the command you want to know about [q for quitting out the app]: " + Style.RESET_ALL).lower()
    if command == "q":
        print(Fore.GREEN + Style.BRIGHT + "Goodbye!" + Style.RESET_ALL)
        break
    elif not command.strip():
        print(Fore.YELLOW + "Please enter a valid command." + Style.RESET_ALL)
        continue
    def recive_info_command(command):
        url = f"https://cheat.sh/{command}?QT"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.MAGENTA + Style.BRIGHT + "\n--- Cheat Sheet Output ---\n" + Style.RESET_ALL)
                print(Fore.WHITE + response.text + Style.RESET_ALL)
                print(Fore.MAGENTA + Style.BRIGHT + "--- End of Output ---\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error fetching cheat sheet." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Request failed: {e}" + Style.RESET_ALL)
    recive_info_command(command)
    choice = input(Fore.CYAN + "Do you want to try the command (y/n): " + Style.RESET_ALL).lower()
    if choice == "y":
        print(Fore.YELLOW + f"\nRunning: {command}\n" + Style.RESET_ALL)
        os.system(command)
    else:
        print(Fore.GREEN + "Okay, not running the command." + Style.RESET_ALL)