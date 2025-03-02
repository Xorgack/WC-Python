import argparse
from details import get_file_details, get_stdin_details
from report import get_state, report, add_details

def main():
    # command line arguments
    parser = argparse.ArgumentParser(description="Unix wc tool written in python")
    parser.add_argument("-v", "--version", action="store_true", help="show version details")
    parser.add_argument("-l", "--lines", action="store_true", help="count newline characters")
    parser.add_argument("-w", "--words", action="store_true", help="count words")
    parser.add_argument("-c", "--bytes", action="store_true", help="count bytes")
    parser.add_argument("-m", "--chars", action="store_true", help="count characters")
    parser.add_argument("-L", "--longest-line", action="store_true", help="count bytes")
    parser.add_argument("--total", type=str, help="show total: auto, always, never")
    parser.add_argument("FILE_PATH", type=str, nargs="*", help="path to the FILE to process")
    args = parser.parse_args()

    # show version
    if args.version:
        print("wc-python v1.0.0\n")
        print("A rewrite of Unix wc tool in python\nWritten by Xorgack")
        quit(0)

    show_total = False

    if args.total:
        match args.total:
            case "auto":
                show_total = len(args.FILE_PATH) > 1
            case "always":
                show_total = True
            case "never":
                show_total = False
            case _:
                print(f"Invalid option for total {args.total}")
                quit(1)
    else:
        show_total = len(args.FILE_PATH) > 1


    # program state
    program_state = get_state(args)

    if not args.FILE_PATH:
        # No path
        stdin_details = get_stdin_details()
        report(stdin_details, program_state, "")
        quit(0)

    # Total
    total_details = {
        "lines": 0,
        "words":0,
        "bytes": 0,
        "longest": 0,
        "chars": 0
    }

    for p in args.FILE_PATH:
        # STDIN
        if p == "-":
            stdin_details = get_stdin_details()
            report(stdin_details, program_state, "-")
            if show_total:
                total_details = add_details(stdin_details, total_details)
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
        
        if show_total:
            total_details = add_details(file_details, total_details)

        
        report(file_details, program_state, p)
    
    if show_total:
        report(total_details, program_state, "total")

    quit(0)

if __name__ == "__main__":
    main()