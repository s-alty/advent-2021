import sys
import re

fold_re = re.compile(r'([xy])=(\d+)')

def parse(it):
    coordinates = []
    for line in it:
        if line == '':
            break
        x,y = line.split(',')
        coordinates.append((int(x), int(y)))

    folds = []
    for line in it:
        match = fold_re.search(line)
        direction, value = match.groups()
        folds.append((direction, int(value)))
    return coordinates, folds

def do_fold(coordinates, fold):
    direction, value = fold
    new_coordinates = []

    if direction == 'y':
        # vertical fold
        for x, y in coordinates:
            if y < value:
                new_coordinates.append((x,y))
            else:
                delta = (y - value)
                new_coordinates.append((x, value-delta))
    else:
        # horizontal fold
        for x, y in coordinates:
            if x < value:
                new_coordinates.append((x, y))
            else:
                delta = (x - value)
                new_coordinates.append((value-delta, y))
    return set(new_coordinates)

def do_all_folds(coordinates, folds):
    for fold in folds:
        coordinates = do_fold(coordinates, fold)
    return coordinates

def get_message(coordinates):
    max_x = max(x for x, _ in coordinates)
    max_y = max(y for _, y in coordinates)

    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            if (x,y) in coordinates:
                line += '#'
            else:
                line += '.'
        print(line)

if __name__ == '__main__':
    coordinates, folds = parse((line.strip() for line in sys.stdin))

    final_coordinates = do_all_folds(coordinates, folds)
    get_message(final_coordinates)
