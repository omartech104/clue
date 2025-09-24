#!/bin/bash

pip install -r requirements.txt --break-system-packages
pyinstaller --onefile --noconfirm --name "clue" main.py
sudo mv dist/clue /usr/bin/
rm -rf build dist clue.spec
mkdir ~/clue_docs
echo "Clue App installed successfully! You can run it using the command 'clue'".
