import os
import sys
import requests
import shutil


def clear_console():
    """Clear the terminal screen in a cross-platform way."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pager_output(text):
    """Show output via pager (less, more, or pydoc), or print if none available."""
    try:
        import pydoc

        pydoc.pager(text)
    except ImportError:
        pager = shutil.which("less") or shutil.which("more")
        if pager:
            import subprocess

            proc = subprocess.Popen([pager], stdin=subprocess.PIPE)
            try:
                proc.communicate(input=text.encode("utf-8"))
            except Exception:
                print(text)
        else:
            print(text)


def fetch_cheat_sheet(cmd):
    """Fetch a cheat sheet from cheat.sh for the given command."""
    url = f"https://cheat.sh/{cmd}?QT"
    try:
        response = requests.get(url, timeout=10)
        if response.ok and response.text.strip():
            return response.text
        return None
    except Exception as e:
        return f"Request failed: {e}"


def command_exists(command):
    """Check if a command exists on the user's system."""
    return shutil.which(command) is not None


def prompt_yes_no(prompt):
    """Prompt the user for a yes/no answer."""
    while True:
        choice = input(f"{prompt} [y/n]: ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main():
    if not sys.platform.startswith("linux"):
        print("This program is designed for Linux systems.")
        sys.exit(1)

    clear_console()
    print("Welcome to Clue! Get instant help for any Linux command.\n")

    while True:
        command = input(
            "Enter the command you want to know about (or type 'quit' to exit): "
        ).strip()
        if not command:
            print("Please enter a command.")
            continue
        if command.lower() == "quit":
            print("Goodbye!")
            break

        if not command_exists(command):
            print(
                f"\n  '{command}' does not exist on your system or is not in your PATH.\n"
            )
            if not prompt_yes_no("Would you like to see the cheat sheet anyway?"):
                continue

        print(f"\nFetching cheat sheet for '{command}'...\n")
        cheat_sheet = fetch_cheat_sheet(command)
        if cheat_sheet:
            pager_output(cheat_sheet)
        else:
            print("No cheat sheet found or unable to fetch information.")

        if prompt_yes_no(f"Do you want to try running '{command}' now?"):
            params = input("Enter any parameters (or press Enter to skip): ").strip()
            full_command = f"{command} {params}".strip()
            print(f"\nRunning: {full_command}\n")
            os.system(full_command)
        else:
            print("Okay, not running the command.")

        input("\nPress Enter to continue...")
        clear_console()


if __name__ == "__main__":
    main()
