import os, sys, requests

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
    
    command = input("Enter the command you want to know about: ").lower()
    def recive_info_command(command):
        url = f"https://cheat.sh/{command}?QT"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(response.text)
            else:
                print("Error fetching cheat sheet.")
        except Exception as e:
            print(f"Request failed: {e}")
    recive_info_command(command)
    choice = input("Do you want to try the command (y/n): ").lower()
    if choice == "y":
        os.system(command)
    else:
        print("Okay, not running the command.")