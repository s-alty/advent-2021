import re
import sys

NUM_ROWS = 1000
NUM_COLS = 1000

line_regex = re.compile(r'^(\d+),(\d+) -> (\d+),(\d+)$')

# represent intersections as grid of counts
def init_count_grid():
    return [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# represent line as a 2-tuple of 2-tuples
def parse_line(l):
    match = line_regex.match(l)
    if not match:
        raise Exception("Invalid line: {}".format(line))
    x1,y1,x2,y2 = match.groups()
    return ((int(x1), int(y1)), (int(x2), int(y2)))

def draw(grid, line):
    ((x1, y1), (x2, y2)) = line

    # either horizontal or vertical
    if x1 != x2:
        # vertical line
        assert y1 == y2

        start = min(x1, x2)
        end = max(x1, x2) + 1
        col = y1
        for i in range(start, end):
            grid[i][col] += 1
    else:
        # horizontal line
        start = min(y1, y2)
        end = max(y1, y2) + 1
        row = x1
        for i in range(start, end):
            grid[row][i] += 1

def count_overlaps(grid):
    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    return count

def is_vertical_or_horizontal(line):
    ((x1, y1), (x2, y2)) = line
    return x1 == x2 or y1 == y2

if __name__ == '__main__':
    grid = init_count_grid()
    parsed = (parse_line(l) for l in sys.stdin)
    valid = (line for line in parsed if is_vertical_or_horizontal(line))
    for line in valid:
        draw(grid, line)

    print(count_overlaps(grid))
