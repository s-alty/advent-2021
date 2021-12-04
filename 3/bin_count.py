import itertools
import sys

# return the first element of the iterable without "consuming" it
def peek(it):
    first = next(it)
    return first, itertools.chain([first], it)

def count_bits(bs_list):
    # see how many bits we need to count
    first, bs_list = peek(bs_list)
    counts = [0 for _ in range(len(first))]

    for bs in bs_list:
        for i, c in enumerate(bs):
            if c == '0':
                counts[i] -= 1
            elif c == '1':
                counts[i] += 1
    return counts

def to_int(bitlist):
    return sum(2**i if b else 0 for i,b in enumerate(bitlist[::-1]))

if __name__ == '__main__':
    bit_counts = count_bits(line.strip() for line in sys.stdin)
    gamma = [(c > 0) for c in bit_counts]
    gamma_int = to_int(gamma)
    epsilon = [not c for c in gamma]
    epsilon_int = to_int(epsilon)
    print(gamma_int * epsilon_int)
