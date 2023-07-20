from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


def main():
    code = '1234'
    state = State.LOCKED
    entry = ''

    # match-case
    while True:
        match state:
            case State.LOCKED:
                entry += input(entry)
                if entry == code:
                    state = State.UNLOCKED
                if not code.startswith(entry):
                    # the code is wrong
                    state = State.FAILED
            case State.UNLOCKED:
                print('\nUNLOCKED')
                break
            case State.FAILED:
                print('\nFAILED')
                entry = ''
                state = State.LOCKED

    # while True:
    #     if state == State.LOCKED:
    #         entry += input(entry)

    #         if entry == code:
    #             state = State.UNLOCKED

    #         if not code.startswith(entry):
    #             # the code is wrong
    #             state = State.FAILED
    #     elif state == State.FAILED:
    #         print('\nFAILED')
    #         entry = ''
    #         state = State.LOCKED
    #     elif state == State.UNLOCKED:
    #         print('\nUNLOCKED')
    #         break

main()