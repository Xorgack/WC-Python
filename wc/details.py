from os.path import exists, isfile
from sys import stdin

def get_file_details(file_path):
    details = {
        "exists": True,
        "is_file": True,
        "lines": 0,
    }

    # Check path validity
    if not exists(file_path):
        details["exists"] = False
        return details
    if not isfile(file_path):
        details["is_file"] = False
        return details
    
    with open(file_path, "r") as data:
        for line in data:
            for c in line:
                if c == "\n":
                    details["lines"] += 1

    return details
    
def get_stdin_details():
    details = {
        "lines": 0,
    }

    data = stdin.read()

    for c in data:
        if c == "\n":
            details["lines"] += 1
    
    return details