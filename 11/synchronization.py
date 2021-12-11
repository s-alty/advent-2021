import sys

flash_count = 0

class octopus:
    def __init__(self, energy):
        self.energy = energy
        self.neighbors = []
        self.flashed = False

    def inc(self):
        if self.flashed:
            # refractory period
            return

        self.energy += 1
        if self.energy == 10:
            self.energy = 0
            self.flashed = True
            global flash_count
            flash_count += 1
            for n in self.neighbors:
                n.inc()

def step(octopi):
    for o in octopi:
        o.inc()

    if all([o.flashed for o in octopi]):
        return True

    # reset
    for o in octopi:
        o.flashed = False
    return False

def get_neighbors(grid, i, j):
    neighbors = []
    try:
        if i - 1 >= 0 and j-1 >= 0:
            neighbors.append(grid[i-1][j-1])
    except IndexError:
        pass
    try:
        if i-1 >= 0:
            neighbors.append(grid[i-1][j])
    except IndexError:
        pass
    try:
        if i - 1 >= 0:
            neighbors.append(grid[i-1][j+1])
    except IndexError:
        pass
    try:
        if j-1 >= 0:
            neighbors.append(grid[i][j-1])
    except IndexError:
        pass
    try:
        neighbors.append(grid[i][j+1])
    except IndexError:
        pass
    try:
        if j-1 >= 0:
            neighbors.append(grid[i+1][j-1])
    except IndexError:
        pass
    try:
        neighbors.append(grid[i+1][j])
    except IndexError:
        pass
    try:
        neighbors.append(grid[i+1][j+1])
    except IndexError:
        pass
    return neighbors

def construct_octopi(lines):
    # first construct the classes, then set the neighbors
    octopi_grid = [[octopus(int(v)) for v in line] for line in lines]

    for i, line in enumerate(octopi_grid):
        for j, o in enumerate(line):
            o.neighbors = get_neighbors(octopi_grid, i, j)
    return octopi_grid

def print_grid(grid):
    for line in grid:
        print(''.join(str(o.energy) for o in line))
    print('\n')

if __name__ == '__main__':
    octopi_grid = construct_octopi((l.strip() for l in sys.stdin))
    all_octopi = [o for row in octopi_grid for o in row]

    step_count = 0
    while True:
        step_count += 1
        if step(all_octopi):
            break
    print(step_count)
