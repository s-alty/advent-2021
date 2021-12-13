import sys

def cost(positions, candidate):
    return sum([abs(candidate - p) for p in positions])

if __name__ == '__main__':
    positions = [int(v) for v in next(sys.stdin).split(',')]

    # TODO: possible to binary search instead?
    candidates = range(min(positions), max(positions))
    costs = [cost(positions, c) for c in candidates]
    print(min(costs))
