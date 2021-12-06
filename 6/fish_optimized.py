import sys

def step(fish):
    # fish is an array of counters
    new_counts = [0 for _ in range(9)]
    for i in range(len(new_counts)):
        new_counts[i] = fish[(i+1) % 9]
        if i == 6:
            new_counts[6] += fish[0]
    return new_counts

def parse_counts(line):
    fish = [int(v) for v in line.split(',')]
    counts = [0 for _ in range(9)]
    for f in fish:
        counts[f] += 1
    return counts

if __name__ == '__main__':
    counts = parse_counts(next(sys.stdin))
    for i in range(256):
        counts = step(counts)
    print(sum(counts))
