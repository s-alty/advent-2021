import itertools
import sys

def triples(it):
    it1, it2, it3 = itertools.tee(it, 3)
    next(it2)
    next(it3)
    next(it3)
    return zip(it1, it2, it3)

def sliding_three_sum(it):
    for first, second, third in triples(it):
        yield int(first) + int(second) + int(third)

def pairs(it):
    # copy the iterator into two output iterators
    it1, it2 = itertools.tee(it)
    # advance the second iterator by one position
    next(it2)

    return zip(it1, it2)

if __name__ == '__main__':
    count = 0
    sliding_window_sum = sliding_three_sum(sys.stdin)
    for first_sum, second_sum in pairs(sliding_window_sum):
        if second_sum > first_sum:
            count += 1
    print(count)
