#!/bin/bash
set -e # stop on first error

# Install dependencies (better to use user scope or venv)
pip install --user -r requirements.txt

# Build the binary
pyinstaller --onefile --noconfirm --name "clue" main.py

sudo mv dist/clue /usr/local/bin/

rm -rf build dist clue.spec

mkdir -p ~/clue_docs

echo "✅ Clue App installed successfully! You can run it using the command: clue"
