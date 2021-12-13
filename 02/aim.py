import sys
from collections import namedtuple

OP = namedtuple('OP', ['direction', 'value'])

def to_op(instruction_str):
    direction, val = instruction_str.split(' ')
    return OP(direction, int(val))


class Sub():
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def apply_op(self, op):
        if op.direction == 'down':
            self.aim += op.value
        elif op.direction == 'up':
            self.aim -= op.value
        elif op.direction == 'forward':
            self.horizontal += op.value
            self.depth += op.value * self.aim

def pilot(instructions):
    sub = Sub()
    for instruction in instructions:
        op = to_op(instruction)
        sub.apply_op(op)
    return sub

if __name__ == '__main__':
    final = pilot(sys.stdin)
    print(final.horizontal * final.depth)
