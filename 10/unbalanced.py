import sys

open_chars = set('([{<')

closing_chars_to_open_chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def first_illegal_character(line):
    chunks = []
    for c in line:
        if c in open_chars:
            chunks.append(c)
        else:
            # it's a closing char, it must match
            match = closing_chars_to_open_chars[c]
            if match == chunks[-1]:
                chunks.pop(-1)
            else:
                return c
    return None

def score(illegals):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    total = 0
    for c in illegals:
        total += points.get(c, 0)
    return total

if __name__ == '__main__':
    illegal_chars = (first_illegal_character(line.strip()) for line in sys.stdin)
    print(score(illegal_chars))
