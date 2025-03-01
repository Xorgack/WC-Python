from enum import Enum

class State(Enum):
    LINES = 1
    WORDS = 2
    BYTES = 4

def get_state(args):
    state = 0
    if args.lines:
        state |= State.LINES.value
    if args.words:
        state |= State.WORDS.value
    if args.bytes:
        state |= State.BYTES.value

    # Return default if no flag provided
    return state or (State.LINES.value | State.WORDS.value | State.BYTES.value)

def report(details, state, title):
    print("", end=" ")

    if state & State.LINES.value:
        print(f"{details['lines']:3}", end="\t")
    if state & State.WORDS.value:
        print(f"{details['words']:3}", end="\t")
    if state & State.BYTES.value:
        print(f"{details['bytes']:3}", end="\t")

    print(title)