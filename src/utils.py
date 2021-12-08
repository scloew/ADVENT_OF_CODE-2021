from operator import lt, ge
from .classes.bingo_board import BingoBoard


def day_3b_util(data, one_tie_breaker):
    compare = ge if one_tie_breaker else lt
    contenders = set(data)
    for i in range(len(data[0])):
        if len(contenders) == 1:
            return contenders.pop()
        ones, zeros = set(), set()
        for bin_num in contenders:
            if bin_num[i] == '1':
                ones.add(bin_num)
            else:
                zeros.add(bin_num)
        contenders = ones if compare(len(ones), len(zeros)) else zeros


def transform_day4_input(data):
    nums_called = (int(i) for i in data[0].split(','))

    grids = ''.join(data[2:]).split('\n\n')
    boards = set()

    for grid in grids:
        grid = grid.split('\n')
        grid = [[int(i) for i in row.strip().replace('  ', ' ').split(' ')] for row in grid]
        boards.add(BingoBoard(grid))
    return nums_called, boards
