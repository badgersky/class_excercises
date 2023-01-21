from chessboard import Chessboard


cb = Chessboard()


class Figure:

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def _check_moves(moves):
        copied_moves = moves.copy()
        for m in moves:
            if m[0] < 0 or m[0] > 7:
                copied_moves.remove(m)
            elif m[1] < 0 or m[1] > 7:
                copied_moves.remove(m)
        return copied_moves

    def _get_diagonal_moves(self, board):
        values = list(range(1, 8))
        allowed_moves = []
        for value in values:
            allowed_moves.append((self.x + value, self.y + value))
            allowed_moves.append((self.x + value, self.y - value))
            allowed_moves.append((self.x - value, self.y + value))
            allowed_moves.append((self.x - value, self.y - value))

        copied_moves = allowed_moves.copy()
        for m in allowed_moves:
            if m == (self.x, self.y):
                copied_moves.remove(m)
            if m[0] < 0 or m[0] > 7:
                copied_moves.remove(m)
            elif m[1] < 0 or m[1] > 7:
                copied_moves.remove(m)
        return copied_moves

    def _get_horizontal_moves(self, board):
        values = list(range(8))
        allowed_moves = []
        for value in values:
            allowed_moves.append((self.x, value))
        for value in values:
            allowed_moves.append((value, self.y))

        for m in allowed_moves:
            if m == (self.x, self.y):
                allowed_moves.remove(m)
        return allowed_moves


class Pawn(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moved = False

    def list_allowed_moves(self, board):
        if self.color.lower() == 'white':
            if self.moved is False:
                return [(self.x, self.y + 1), (self.x, self.y + 2)]
            elif self.moved is True and self.y < 7:
                return [(self.x, self.y + 1)]
            else:
                return []
        elif self.color.lower() == 'black':
            if self.moved is False:
                return [(self.x, self.y - 1), (self.x, self.y - 2)]
            elif self.moved is True and self.y > 0:
                return [(self.x, self.y - 1)]
            else:
                return []

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            super().move(x, y)
        if self.moved is False:
            self.moved = True


class Knight(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def list_allowed_moves(self, board):
        allowed_moves = [
                (self.x - 2, self.y - 1),
                (self.x - 1, self.y - 2),
                (self.x - 2, self.y + 1),
                (self.x - 1, self.y + 2),
                (self.x + 1, self.y + 2),
                (self.x + 2, self.y + 1),
                (self.x + 2, self.y - 1),
                (self.x + 1, self.y - 2)
            ]

        return super()._check_moves(allowed_moves)

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            super().move(x, y)


class Rook(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def list_allowed_moves(self, board):
        return super()._get_horizontal_moves(cb)

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            super().move(x, y)


class King(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def list_allowed_moves(self, board):
        allowed_moves = [
            (self.x + 1, self.y),
            (self.x + 1, self.y - 1),
            (self.x, self.y - 1),
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y),
            (self.x - 1, self.y + 1),
            (self.x, self.y + 1),
            (self.x + 1, self.y + 1)
        ]

        return super()._check_moves(allowed_moves)

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            super().move(x, y)


class Bishop(Figure):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def list_allowed_moves(self, board):
        return super()._get_diagonal_moves(cb)

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            super().move(x, y)
