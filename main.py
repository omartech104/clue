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