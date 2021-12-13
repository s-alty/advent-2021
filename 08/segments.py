import sys


def parse(line):
    segments, display = line.split('|')
    return [set(s) for s in segments.split()], [set(s) for s in display.split()]

def has_unique_segment_number(display_value):
    return len(display_value) in {2, 4, 3, 7}

if __name__ == '__main__':
    displays = (parse(line)[1] for line in sys.stdin)
    unique_output_segments = [d for display in displays for d in display if has_unique_segment_number(d)]
    print(len(unique_output_segments))
