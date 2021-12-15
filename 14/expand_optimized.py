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

def counts(s):
    counts = collections.Counter()
    for c1, c2 in pairwise(s):
        counts[c1+c2] += 1
    return counts

def expand(digram_counts, individual_counts, expansions):
    new_digram_counts = collections.Counter()
    for digram, old_count in digram_counts.most_common():
        insertion_char = expansions[digram]
        new_digram_counts[digram[0]+insertion_char] += old_count
        new_digram_counts[insertion_char+digram[1]] += old_count
        individual_counts[insertion_char] += old_count
    return new_digram_counts, individual_counts


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

    digram_counts = counts(initial)
    individual_counts = collections.Counter(initial)
    for _ in range(40):
        digram_counts, individual_counts = expand(digram_counts, individual_counts, expansions)


    most_common = individual_counts.most_common()
    print(most_common[0][1] - most_common[-1][1])
