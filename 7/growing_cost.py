import sys

def single_cost(position, candidate):
    n = abs(candidate - position)
    # closed form for sum from 1 to n
    return int((n * (n+1)) / 2)

def cost(positions, candidate):
    return sum([single_cost(p, candidate) for p in positions])

if __name__ == '__main__':
    positions = [int(v) for v in next(sys.stdin).split(',')]

    # TODO: possible to binary search instead?
    candidates = range(min(positions), max(positions))
    costs = [cost(positions, c) for c in candidates]
    print(min(costs))
