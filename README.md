
# Clue App

## Overview
Clue is a command-line tool for Linux that helps users look up command usage and explanations using the cheat.sh API. It presents results in a plain, readable style and saves each command's documentation to a text file. You can also try out the command directly from the app.

## Features
- Prompts the user to enter a command they want to know about
- Fetches and displays the cheat sheet for the entered command from cheat.sh
- Presents output in a plain, readable style with clear separators
- Saves each command's documentation to `doc.txt` in the project folder
- Optionally runs the entered command in the terminal
- Clears the screen before showing output so documentation starts at the top
- Handles errors gracefully if the API is unreachable or the command is not found

## How It Works
1. The app checks the operating system and runs only on Linux.
2. The user is prompted to enter a command.
3. The app sends a request to the cheat.sh API using the entered command and displays the result in a plain format, with headers and separators.
4. The documentation for the command is saved to `doc.txt`.
5. The user is asked if they want to try running the command. If yes, the command is executed in the terminal.

## Example Usage
```
$ python main.py
Enter the command you want to know about [quit for quiting out the app]: ls

-----------------------------
Command: ls
-----------------------------
[cheat.sh output for 'ls']
-----------------------------

Do you want to try the command (y/n): y
[output of 'ls' command]
```

## Requirements
- Python 3
- run the installation script (`./install.sh`)
- Linux operating system
- [bat](https://github.com/sharkdp/bat) and [less](https://github.com/gwsw/less) for paging, [installtion here for both](https://github.com/omartech104/clue/blob/main/docs/Installing_Bat.md)
## Limitations
- The app does not run on Windows or macOS.
- Requires an active internet connection to fetch cheat sheets.
- Running commands is limited to those available in the Linux shell.

## License
This project is for personal use and learning purposes.
