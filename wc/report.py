from enum import Enum

class State(Enum):
    LINES = 1

def get_state(args):
    state = 0
    if args.lines:
        state |= State.LINES.value
    return state

def report(details, state, title):
    print("", end=" ")
    if state & State.LINES.value:
        print(f"{details['lines']:3}", end="\t")
    print(title)