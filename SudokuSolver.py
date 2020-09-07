from pprint import pprint
from PerformanceTimer import timeit


def get_row(board, r):
    return board[r]


def get_col(board, c):
    arr = []
    for r in range(9):
        arr.append(board[r][c])
    return arr


def get_square(board, n):
    arr = []
    start_r = 3 * (n // 3)
    start_c = 3 * (n % 3)
    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            arr.append(board[r][c])
    return arr


def find_next_zero(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return row, col
    return None, None


def solve(board):
    # find first 0
    # loop 1-9 until correct
    # if not correct, go back up the stack
    r, c = find_next_zero(board)
    if r is None:  # if no more zeroes
        return True

    for i in range(1, 10):
        board[r][c] = i
        # pprint(board)
        if verify(board):
            if solve(board):
                return True

    # could not find a valid solution. Go back up the stack
    board[r][c] = 0
    return False


def verify(board):
    # check cols, rows, boxes for any inconsistencies
    for n in range(9):
        row = get_row(board, n)
        col = get_col(board, n)
        square = get_square(board, n)
        for i in range(1, 10):
            if row.count(i) > 1:
                return False
            if col.count(i) > 1:
                return False
            if square.count(i) > 1:
                return False
    return True


@timeit
def main():
    grid = [[0, 8, 0, 0, 0, 0, 2, 4, 7],
            [0, 1, 4, 2, 0, 0, 0, 0, 0],
            [0, 7, 2, 8, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 7, 0, 8, 0],
            [7, 0, 8, 4, 0, 3, 1, 0, 2],
            [0, 2, 0, 9, 0, 0, 0, 0, 0],
            [0, 0, 7, 0, 0, 6, 4, 3, 0],
            [0, 0, 0, 0, 0, 2, 7, 6, 0],
            [9, 6, 3, 0, 0, 0, 0, 2, 0]]
    solve(grid)
    pprint(grid)


if __name__ == '__main__':
    main()
