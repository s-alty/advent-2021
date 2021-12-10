import sys
import itertools

def build_grid(lines):
    return [[int(c) for c in line.strip()] for line in lines]

def basin_size(grid, current_row, current_col, visited):
    if (current_row, current_col) in visited:
        # don't double count
        return 0

    current_val = grid[current_row][current_col]
    # 9 is never part of a basin
    if current_val == 9:
        return 0

    visited.add((current_row, current_col))

    # north
    north = 0
    north_row = current_row - 1
    north_col = current_col
    if north_row >= 0:
        north = basin_size(grid, north_row, north_col, visited)

    # south
    south = 0
    south_row = current_row + 1
    south_col = current_col
    if south_row < len(grid):
        south = basin_size(grid, south_row, south_col, visited)

    # east
    east = 0
    east_row = current_row
    east_col = current_col + 1
    if east_col < len(grid[current_row]):
        east = basin_size(grid, east_row, east_col, visited)

    # west
    west = 0
    west_row = current_row
    west_col = current_col - 1
    if west_col >= 0:
        west = basin_size(grid, west_row, west_col, visited)

    return 1 + north + south + east + west

def basin_sizes(grid):
    low_points = find_low_points(grid)
    return [basin_size(grid, row, col, set()) for row, col in low_points]

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

def find_low_points(grid):
    low_points = []
    row_index = 0
    for prev, current, successor in neighboring_lines(iter(grid)):
        for i, val in enumerate(current):
            if is_low_point(prev, current, successor, i, val):
                low_points.append((row_index, i))
        row_index += 1
    return low_points

if __name__ == '__main__':
    grid = build_grid(sys.stdin)
    # multiply three largest basins
    basins = list(reversed(sorted(basin_sizes(grid))))
    print(basins[0] * basins[1] * basins[2])
