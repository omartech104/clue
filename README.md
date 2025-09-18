
# Clue App

## Overview
Clue is a command-line tool for Linux that helps users look up command usage and explanations using the cheat.sh API. It also allows users to try out the command directly from the app.

## Features
- Prompts the user to enter a command they want to know about
- Fetches and displays the cheat sheet for the entered command from cheat.sh
- Optionally runs the entered command in the terminal
- Clears the screen for a clean user interface (Linux only)
- Handles errors gracefully if the API is unreachable or the command is not found

## How It Works
1. The app checks the operating system and runs only on Linux.
2. The user is prompted to enter a command.
3. The app sends a request to the cheat.sh API using the entered command and displays the result.
4. The user is asked if they want to try running the command. If yes, the command is executed in the terminal.

## Example Usage
```
$ python main.py
Enter the command you want to know about [q for quiting out the app]: ls
[cheat.sh output for 'ls']
Do you want to try the command (y/n): y
[output of 'ls' command]
```

## Requirements
- Python 3
- requests library (`pip install -r reqiurements.txt`)
- Linux operating system

## Limitations
- The app does not run on Windows or macOS.
- Requires an active internet connection to fetch cheat sheets.
- Running commands is limited to those available in the Linux shell.

## License
This project is for personal use and learning purposes.
