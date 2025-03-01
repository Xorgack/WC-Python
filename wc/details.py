from os.path import exists, isfile
from sys import stdin

def get_file_details(file_path):
    details = {
        "exists": True,
        "is_file": True,
    }
    # Check path validity
    if not exists(file_path):
        details["exists"] = False
        return details
    if not isfile(file_path):
        details["is_file"] = False
        return details
    
def get_stdin_details():
    data = stdin.read()