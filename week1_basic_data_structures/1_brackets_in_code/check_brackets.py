# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(char=next, position=i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            
            recent_opening_brackets = opening_brackets_stack.pop()
            match = are_matching(recent_opening_brackets.char, next)
            if not match:
                return i + 1
    
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        recent_opening_brackets = opening_brackets_stack.pop()
        return recent_opening_brackets.position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
