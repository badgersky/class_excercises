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
