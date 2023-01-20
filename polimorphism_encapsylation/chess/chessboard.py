class Chessboard:

    def __init__(self, color):
        self.color = color
        self.board = [[None for _ in range(8)] for _ in range(8)]
