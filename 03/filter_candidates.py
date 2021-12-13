import sys

def most_common(candidate_val, balance):
    if balance >= 0:
        return candidate_val == '1'
    return candidate_val == '0'

def least_common(candidate_val, balance):
    if balance >= 0:
        return candidate_val == '0'
    return candidate_val == '1'


def filter_candidates(candidates, bit_pos, predicate):
    balance = 0
    for candidate in candidates:
        if candidate[bit_pos] == '0':
            balance -= 1
        elif candidate[bit_pos] == '1':
            balance += 1
    return [c for c in candidates if predicate(c[bit_pos], balance)]


def get_rating(bitstrings, predicate):
    index = 0
    candidates = bitstrings
    while(len(candidates)) > 1:
        candidates = filter_candidates(candidates, index, predicate)
        index += 1
    return candidates[0]

def oxygen_rating(bitstrings):
    return get_rating(bitstrings, most_common)

def co2_rating(bitstrings):
    return get_rating(bitstrings, least_common)

if __name__ == '__main__':
    all_values = [line.strip() for line in sys.stdin]
    o = int(oxygen_rating(all_values), 2)
    c = int(co2_rating(all_values), 2)
    print(o * c)
