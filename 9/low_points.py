import sys
import itertools

def build_grid(lines):
    return [[int(c) for c in line.strip()] for line in lines]

def neighboring_lines(it):
    prev = None
    current = next(it)
    successor = next(it)
    while True:
        yield prev, current, successor
        prev = current
        current = successor
        try:
            successor = next(it)
        except StopIteration:
            yield prev, current, None
            break

def is_low_point(prev, current, successor, index, val):
    if prev and prev[index] <= val:
        return False
    if successor and successor[index] <= val:
        return False

    if index - 1 >= 0 and current[index-1] <= val:
        return False

    if index + 1 < len(current) and current[index+1] <= val:
        return False
    return True

def low_points(grid):
    low_points = []
    for prev, current, successor in neighboring_lines(iter(grid)):
        for i, val in enumerate(current):
            if is_low_point(prev, current, successor, i, val):
                low_points.append(val)
    return low_points

if __name__ == '__main__':
    grid = build_grid(sys.stdin)
    points = low_points(grid)
    print(sum(p+1 for p in points))
