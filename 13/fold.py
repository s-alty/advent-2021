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
    return new_coordinates

if __name__ == '__main__':
    coordinates, folds = parse((line.strip() for line in sys.stdin))

    new_coordinates = do_fold(coordinates, folds[0])
    print(len(set(new_coordinates)))
