import itertools
import sys

def pairs(it):
    # copy the iterator into two output iterators
    it1, it2 = itertools.tee(it)
    # advance the second iterator by one position
    next(it2)

    return zip(it1, it2)

if __name__ == '__main__':
    count = 0
    for first, second in pairs(sys.stdin):
        if int(second) > int(first):
            count += 1
    print(count)
