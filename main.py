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
    if command:
        url = f"https://cheat.sh/{command}?QT"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(response.text)
                input("Press Enter to continue...")
            else:
                print("Error fetching cheat sheet.")
        except Exception as e:
            print(f"Request failed: {e}")