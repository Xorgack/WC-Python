import argparse
from details import get_file_details, get_stdin_details
from report import get_state, report

def main():
    # command line arguments
    parser = argparse.ArgumentParser(description="Unix wc tool written in python")
    parser.add_argument("-v", "--version", action="store_true", help="show version details")
    parser.add_argument("-l", "--lines", action="store_true", help="count newline characters")
    parser.add_argument("-w", "--words", action="store_true", help="count words")
    parser.add_argument("FILE_PATH", type=str, nargs="*", help="path to the FILE to process")
    args = parser.parse_args()

    # show version
    if args.version:
        print("wc-python v1.0.0\n")
        print("A rewrite of Unix wc tool in python\nWritten by Xorgack")
        quit(0)

    # program state
    program_state = get_state(args)

    if not args.FILE_PATH:
        # No path
        stdin_details = get_stdin_details()
        report(stdin_details, program_state, "")
        quit(0)

    for p in args.FILE_PATH:
        # STDIN
        if p == "-":
            stdin_details = get_stdin_details()
            report(stdin_details, program_state, "-")
            continue
        file_details = get_file_details(p)
        # Non-existant file
        if not file_details["exists"]:
            print(f"{p}: No such file or directory")
            continue
        # Directory
        if not file_details["is_file"]:
            print(f"{p}: The provided path is a directory")
            continue
        
        report(file_details, program_state, p)

    quit(0)

if __name__ == "__main__":
    main()