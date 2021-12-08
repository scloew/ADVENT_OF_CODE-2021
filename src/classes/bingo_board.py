class BingoBoard:

    def __init__(self, board):
        self._hash_key = str(board)
        self._locations = {}
        self.board = board
        self._build_locations()

    def _build_locations(self):
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                self._locations[val] = (y, x)

    def check_number(self, num):
        location = self._locations.get(num)
        if location is None:
            return False
        y, x, winner = *location, True
        self.board[y][x] = True

        for row in self.board:
            if row[x] is not True:
                winner = False
                break

        if winner:
            return True

        for i in self.board[y]:
            if i is not True:
                return False
        return True

    def calc_score(self):
        sum_ = 0
        for row in self.board:
            sum_ += sum(i for i in row if i is not True)
        return sum_

    def __str__(self):
        return '\n'.join([','.join(str(i) for i in row) for row in self.board])

    def __hash__(self):
        return hash(self._hash_key)
