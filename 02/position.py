import sys
from collections import namedtuple

OP = namedtuple('OP', ['direction', 'value'])

def to_op(instruction_str):
    direction, val = instruction_str.split(' ')
    return OP(direction, int(val))

def apply_op(op, initial_position):
    horizontal, depth = initial_position
    if op.direction == 'forward':
        horizontal += op.value
    elif op.direction == 'down':
        depth += op.value
    elif op.direction == 'up':
        depth -= op.value
    return horizontal, depth

def pilot(instructions):
    position = 0, 0
    for instruction in instructions:
        op = to_op(instruction)
        position = apply_op(op, position)
    return position

if __name__ == '__main__':
    horizontal, depth = pilot(sys.stdin)
    print(horizontal * depth)
