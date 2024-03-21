import os
import platform
import sys

if platform.system() == "Linux":
    os.system('clear')
else:
    os.system('cls')

def list_files():
    _DIR = "/var/log"
    for item in os.listdir(_DIR):
        path = os.path.join(_DIR, item)
        if os.path.isfile(path):
            print(f"{path} is a file")
        else:
            print(f"{path} is a directory")

list_files()