import sys

def populate_1_4_7_and_8(all_segments):
    unidentified = []
    mapping = {}
    for s in all_segments:
        if len(s) == 2:
            mapping[s] = '1'
        elif len(s) == 3:
            mapping[s] = '7'
        elif len(s) == 4:
            mapping[s] = '4'
        elif len(s) == 7:
            mapping[s] = '8'
        else:
            unidentified.append(s)
    return mapping, unidentified

# this depdend of having a representation for 1
def populate_3_and_6(wires_to_digit, unidentified):
    representation_of_1 = {v:k for k,v in wires_to_digit.items()}['1']

    new_unidentified = []
    for s in unidentified:
        if len(s) == 5 and representation_of_1 < s:
            wires_to_digit[s] = '3'
        elif len(s) == 6 and not representation_of_1 < s:
            wires_to_digit[s] = '6'
        else:
            new_unidentified.append(s)
    return new_unidentified

# this depends on having a representation of 4 and elimination of 6
def populate_0_and_9(wires_to_digit, unidentified):
    representation_of_4 = {v:k for k,v in wires_to_digit.items()}['4']
    new_unidentified = []
    for s in unidentified:
        if len(s) == 6:
            if representation_of_4 < s:
                wires_to_digit[s] = '9'
            else:
                wires_to_digit[s] = '0'
        else:
            new_unidentified.append(s)
    return new_unidentified

# depende on having 6 identified
def populate_2_and_5(wires_to_digit, unidentified):
    assert len(unidentified) == 2
    representation_of_6 = {v:k for k,v in wires_to_digit.items()}['6']
    for s in unidentified:
        if s < representation_of_6:
            wires_to_digit[s] = '5'
        else:
            wires_to_digit[s] = '2'

def build_map(segments):
    # return a map that translates a set of wires into a digit
    wires_to_digit, unidentified = populate_1_4_7_and_8(segments)
    new_unidentified = populate_3_and_6(wires_to_digit, unidentified)
    new_unidentified = populate_0_and_9(wires_to_digit, new_unidentified)
    populate_2_and_5(wires_to_digit, new_unidentified)
    return wires_to_digit


def decode(segments, display):
    wires_to_digit = build_map(segments)
    output = ''
    for d in display:
        output += wires_to_digit[d]
    return int(output)

def parse(line):
    segments, display = line.split('|')
    return [frozenset(s) for s in segments.split()], [frozenset(s) for s in display.split()]

if __name__ == '__main__':
    parsed = (parse(line) for line in sys.stdin)
    print(sum(decode(segments, display) for segments, display in parsed))
