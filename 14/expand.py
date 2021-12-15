import collections
import itertools
import re
import sys

expansion_pattern = re.compile(r'(\w\w) -> (\w)')

def pairwise(s):
    it = iter(s)
    first, second = itertools.tee(it)
    next(second)
    return zip(first, second)

def expand(s, expansions):
    result = ''
    for c1, c2 in pairwise(s):
        result += c1
        result += expansions[c1+c2]
    result += s[-1]
    return result


def parse(it):
    initial = next(it)
    # blank line
    next(it)
    expansions = {}
    for line in it:
        match = expansion_pattern.match(line)
        pair, result = match.groups()
        expansions[pair] = result
    return initial, expansions


if __name__ == '__main__':
    initial, expansions = parse(line.strip() for line in sys.stdin)
    s = initial
    for _ in range(10):
        s = expand(s, expansions)

    counts = collections.Counter(s).most_common()
    print(counts[0][1] - counts[-1][1])
