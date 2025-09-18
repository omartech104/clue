import os, sys, requests

running = True
pltform = sys.platform
DOC_FILE = "doc.txt"

def clear_console():
    if pltform == "linux":
        os.system("clear")
    elif pltform == "win32":
        os.system("cls")

while running:
    if pltform == "win32":
        running = False
        print("This program only runs on Linux")
        break

    command = input("Enter the command you want to know about [quit for quitting out the app]: ").lower()
    
    if not os.path.exists(DOC_FILE):
        with open(DOC_FILE, "w", encoding="utf-8") as f:
            f.write("# Command Documentation\n\n")
    
    if command == "quit":
        print("Goodbye!")
        break

    def recive_info_command(command):
        url = f"https://cheat.sh/{command}?QT"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(DOC_FILE, "a", encoding="utf-8") as f:
                    f.write(f"-----------------------------\nCommand: {command}\n-----------------------------\n{response.text}\n-----------------------------\n")
                
                # ✅ Clear the console before showing output
                clear_console()

                print("\n-----------------------------")
                print(f"Command: {command}")
                print("-----------------------------")
                print(response.text)
                print("-----------------------------\n")
            else:
                print("Error fetching cheat sheet.")
        except Exception as e:
            print(f"Request failed: {e}")

    recive_info_command(command)

    choice = input("Do you want to try the command (y/n): ").lower()
    if choice == "y":
        params = input("Enter any parameters for the command (or press Enter to skip): ")
        full_command = f"{command} {params}".strip()
        os.system(full_command)
    else:
        print("Okay, not running the command.")
    input("Press Enter to continue...")
    clear_console()