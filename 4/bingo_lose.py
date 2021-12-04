import sys

NUM_ROWS = 5
NUM_COLS = 5


def make_one_board(board_lines):
    # a list of sets where each set represents either a row or a column
    sets = []

    rows = []
    for line in board_lines:
        rows.append([int(v) for v in line.split()])

    # build the horizontal sets
    for row in rows:
        sets.append(set(row))

    # build vertical sets
    for i in range(NUM_COLS):
        sets.append(set([r[i] for r in rows]))

    return sets


def check(board, selected_numbers):
    # iterate over all of the row and column sets
    # it's a winner if the board set is contained in the slected_numbers
    return any((board_set <= selected_numbers) for board_set in board)

def score(winning_board, selected_numbers, last_selection):
    all_board_numbers = set()
    for s in winning_board:
        all_board_numbers = all_board_numbers | s

    unselected_numbers = all_board_numbers - selected_numbers
    return sum(unselected_numbers) * last_selection

def last_winner(selections, boards):
    for i in range(NUM_COLS, len(selections)):
        selected_numbers = set(selections[:i])

        # filter out winners
        boards = [b for b in boards if not check(b, selected_numbers)]

        if len(boards) == 1:
            # iterate on selections until it wins
            # TODO break this out into a different function?
            final_board = boards[0]
            while not check(final_board, selected_numbers):
                i += 1
                selected_numbers = set(selections[:i])
            return final_board, selected_numbers
    raise Exception("last winner is not unique")


def take(it, n):
    for _ in range(n):
        yield next(it)

def parse(lines):
    selections = [int(v) for v in next(lines).split(',')]
    boards = []

    while True:
        try:
            next(lines) # empty line delimiter
        except StopIteration:
            break
        else:
            boards.append(make_one_board(take(lines, NUM_ROWS)))

    return selections, boards


if __name__ == '__main__':
    selections, boards = parse(sys.stdin)
    winner, selected = last_winner(selections, boards)
    last_selection = selections[len(selected) - 1]
    print(score(winner, selected, last_selection))
