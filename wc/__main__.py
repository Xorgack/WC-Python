import argparse

def main():
    # command line arguments
    parser = argparse.ArgumentParser(description="Unix wc tool written in python")
    parser.add_argument("-v", "--version", action="store_true", help="show version details")
    args = parser.parse_args()

    # show version
    if args.version:
        print("wc-python v1.0.0\n")
        print("A rewrite of Unix wc tool in python\nWritten by Xorgack")
        quit(0)

if __name__ == "__main__":
    main()