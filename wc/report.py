from enum import Enum

class State(Enum):
    LINES = 1
    WORDS = 2

def get_state(args):
    state = 0
    if args.lines:
        state |= State.LINES.value
    if args.words:
        state |= State.WORDS.value
    return state

def report(details, state, title):
    print("", end=" ")
    if state & State.LINES.value:
        print(f"{details['lines']:3}", end="\t")
    if state & State.WORDS.value:
        print(f"{details['words']:3}", end="\t")
    print(title)