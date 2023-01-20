from chessboard import Chessboard


cb = Chessboard()


class Pawn:

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
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
            self.x = x
            self.y = y
        if self.moved is False:
            self.moved = True


class Knight:

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

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
        copied_moves = allowed_moves.copy()
        for m in allowed_moves:
            if m[0] < 0 or m[0] > 7:
                copied_moves.remove(m)
            elif m[1] < 0 or m[1] > 7:
                copied_moves.remove(m)
        return copied_moves

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            self.x = x
            self.y = y


class Rook:

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

    def list_allowed_moves(self, board):
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

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            self.x = x
            self.y = y


class King:

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color

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

        copied_moves = allowed_moves.copy()
        for m in allowed_moves:
            if m[0] < 0 or m[0] > 7:
                copied_moves.remove(m)
            elif m[1] < 0 or m[1] > 7:
                copied_moves.remove(m)
        return copied_moves

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            self.x = x
            self.y = y
