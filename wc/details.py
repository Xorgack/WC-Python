from os.path import exists, isfile, getsize
from sys import stdin

def get_file_details(file_path):
    details = {
        "exists": True,
        "is_file": True,
        "lines": 0,
        "words": 0,
        "bytes": 0,
    }

    # Check path validity
    if not exists(file_path):
        details["exists"] = False
        return details
    if not isfile(file_path):
        details["is_file"] = False
        return details
    
    # Get size
    details["bytes"] += getsize(file_path)


    with open(file_path, "r") as data:
        for line in data:
            in_word = False
            for c in line:
                if not c.isspace():
                    in_word = True
                elif in_word:
                    in_word = False
                    details["words"] += 1
                if c == "\n":
                    details["lines"] += 1

    return details
    
def get_stdin_details():
    details = {
        "lines": 0,
        "words":0,
        "bytes": 0,
    }

    try:
        line = stdin.readline()
        while line:
            details["bytes"] += len(line)

            in_word = False
            for c in line:
                if not c.isspace():
                    in_word = True
                elif in_word:
                    in_word = False
                    details["words"] += 1
                if c == "\n":
                    details["lines"] += 1

            line = stdin.readline()
    except KeyboardInterrupt:
        pass

    return details