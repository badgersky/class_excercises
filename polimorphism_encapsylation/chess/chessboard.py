class Chessboard:

    def __init__(self, color='white'):
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
        