import sys

def step(fish):
    results = []
    births = 0
    for f in fish:
        if f == 0:
            f = 6
            births += 1
        else:
            f -= 1
        results.append(f)

    return results + [8 for _ in range(births)]


if __name__ == '__main__':
    fish = [int(f) for f in next(sys.stdin).split(',')]
    for i in range(80):
        fish = step(fish)
    print(len(fish))
