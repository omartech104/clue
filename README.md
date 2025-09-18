# Clue App

## Overview
Clue is a simple command-line tool that helps users quickly look up command usage and explanations using the cheat.sh API. It is designed to run on Linux systems and provides instant access to cheat sheets for various commands.

## Features
- Prompts the user to enter a command they want to know about
- Fetches and displays the cheat sheet for the entered command from cheat.sh
- Clears the screen for a clean user interface (Linux only)
- Handles errors gracefully if the API is unreachable or the command is not found

## How It Works
1. The app checks the operating system and runs only on Linux.
2. The user is prompted to enter a command.
3. The app sends a request to the cheat.sh API using the entered command.
4. The cheat sheet for the command is displayed in the terminal.

## Example Usage
```
$ python main.py
Enter the command you want to know about: ls
[cheat.sh output for 'ls']
```

## Requirements
- Python 3
- requests library (`pip install requests`)
- Linux operating system

## Limitations
- The app does not run on Windows or macOS.
- Requires an active internet connection to fetch cheat sheets.

## License
This project is for personal use and learning purposes.
