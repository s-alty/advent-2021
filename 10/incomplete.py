import sys

open_chars = set('([{<')

closing_chars_to_open_chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

open_chars_to_closing_chars = {v:k for k,v in closing_chars_to_open_chars.items()}


def completion(line):
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
                # corrupt
                return None
    return [open_chars_to_closing_chars[c] for c in reversed(chunks)]

def score(completion):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    total = 0
    for c in completion:
        total *= 5
        total += points[c]
    return total

if __name__ == '__main__':
    completions = (completion(line.strip()) for line in sys.stdin)
    scores = list(sorted([score(completion) for completion in completions if completion is not None]))
    print(scores[len(scores) // 2])
