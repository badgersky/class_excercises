import figures as f


class Chessboard:

    def __init__(self):
        color = 'white'
        self._color = color
        self.board = [[None for _ in range(8)] for _ in range(8)]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        if c.lower() not in ['white', 'black']:
            raise ValueError(f'Invalid color: {c}')
        self._color = c

    @staticmethod
    def _create_white_figures():
        color = 'white'
        white_pawns = [f.Pawn(color, i, 1) for i, _ in enumerate(range(8))]
        king = f.King(color, 4, 0)
        queen = f.Queen(color, 3, 0)
        other_figures = [
            f.Rook(color, 0, 0),
            f.Knight(color, 1, 0),
            f.Bishop(color, 2, 0),
            king,
            queen,
            f.Bishop(color, 5, 0),
            f.Knight(color, 6, 0),
            f.Rook(color, 7, 0)
        ]
        return white_pawns, other_figures

    @staticmethod
    def _create_black_figures():
        color = 'black'
        black_pawns = [f.Pawn(color, i, 6) for i, _ in enumerate(range(8))]
        king = f.King(color, 4, 7)
        queen = f.Queen(color, 3, 7)
        other_figures = [
            f.Rook(color, 0, 7),
            f.Knight(color, 1, 7),
            f.Bishop(color, 2, 7),
            king,
            queen,
            f.Bishop(color, 5, 7),
            f.Knight(color, 6, 7),
            f.Rook(color, 7, 7)
        ]
        return black_pawns, other_figures

    def setup(self):
        black_pawns, black_figures = self._create_black_figures()
        white_pawns, white_figures = self._create_white_figures()
        for c, col in enumerate(self.board):
            for r, row in enumerate(self.board):
                if r == 0:
                    self.board[c][r] = white_figures[c]
                elif r == 1:
                    self.board[c][r] = white_pawns[c]
                elif r == 6:
                    self.board[c][r] = black_pawns[c]
                elif r == 7:
                    self.board[c][r] = black_figures[c]
        return self.board

    def list_allowed_moves(self, x, y):
        figure = self.board[x][y]
        if figure is None:
            return None
        if self.color != figure.color:
            return None
        return figure.list_allowed_moves(self.board)

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)
        if allowed_moves is not None:
            if (to_x, to_y) in allowed_moves:
                figure = self.board[from_x][from_y]
                figure.move(to_x, to_y)
                self.board[to_x][to_y] = figure
                self.board[from_x][from_y] = None
        else:
            raise ValueError(f'Invalid move: {to_x, to_y}')

        if self._color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'


if __name__ == '__main__':
    cb = Chessboard()
    cb.setup()
    cb.color = 'black'
    cb.move(0, 6, 0, 4)
    print(cb.color)
    print(cb.board[0][4])

