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
            elif self.moved is True and self.y < 7:
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

    def __init__(self, color, y, x):
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
        for move in allowed_moves:
            if move[0] > 7 or move[1] > 7:
                allowed_moves.remove(move)
            if move[0] < 0 or move[1] < 0:
                allowed_moves.remove(move)
        return allowed_moves

    def move(self, x, y):
        if (x, y) in self.list_allowed_moves(cb):
            self.x = x
            self.y = y
