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
    grid[x1][y1] += 1
    while x1 != x2 or y1 != y2:
        if x1 != x2:
            # move one closer x
            x1 += 1 * (-1 if x1 > x2 else 1)
        if y1 != y2:
            # move one closer y
            y1 += 1 * (-1 if y1 > y2 else 1)
        grid[x1][y1] += 1



def count_overlaps(grid):
    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    return count


if __name__ == '__main__':
    grid = init_count_grid()
    parsed = (parse_line(l) for l in sys.stdin)
    for line in parsed:
        draw(grid, line)

    print(count_overlaps(grid))
