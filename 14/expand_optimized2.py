import collections
import itertools
import re
import sys
import functools
import cProfile

expansion_pattern = re.compile(r'(\w\w) -> (\w)')
expansions = {}

def pairwise(s):
    it = iter(s)
    first, second = itertools.tee(it)
    next(second)
    return zip(first, second)

@functools.lru_cache(maxsize=2**16)
def expand_small(s):
    result = ''
    for c1, c2 in pairwise(s):
        result += c1
        result += expansions[c1+c2]
    result += s[-1]
    return result


def expand(s):
    l = len(s)
    if l <= 512:
        return expand_small(s)

    # else we need to divide into subproblems
    split_point = l // 2
    half1 = s[:split_point]
    half2 = s[split_point:]
    middle_expansion = expansions[half1[-1] + half2[0]]
    return expand(half1) + middle_expansion + expand(half2)

def parse(it):
    initial = next(it)
    # blank line
    next(it)
    for line in it:
        match = expansion_pattern.match(line)
        pair, result = match.groups()
        expansions[pair] = result
    return initial


if __name__ == '__main__':
    initial = parse(line.strip() for line in sys.stdin)

    s = initial
    for i in range(25):
        s = expand(s)

    counts = collections.Counter(s).most_common()
    print(counts[0][1] - counts[-1][1])
