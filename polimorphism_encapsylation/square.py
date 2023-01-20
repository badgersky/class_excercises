class Square:

    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * (2**0.5)

    @property
    def side(self):
        return f'{self._side:.2f}'

    @side.setter
    def side(self, value):
        if type(value) not in [int, float]:
            raise TypeError(f'Invalid value for side: {value}')
        if value < 0:
            raise ValueError(f'Invalid value for side: {value}')
        self._side = value
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * (2**0.5)

    @property
    def perimeter(self):
        return f'{self._perimeter:.2f}'

    @perimeter.setter
    def perimeter(self, value):
        if type(value) not in [int, float]:
            raise TypeError(f'Invalid value for perimeter: {value}')
        if value < 0:
            raise ValueError(f'Invalid value for perimeter: {value}')
        self._perimeter = value
        self._side = self._perimeter / 4
        self._area = self._side ** 2
        self._diagonal = self._side * (2 ** 0.5)

    @property
    def area(self):
        return f'{self._area:.2f}'

    @area.setter
    def area(self, value):
        if type(value) not in [int, float]:
            raise TypeError(f'Invalid value for area: {value}')
        if value < 0:
            raise ValueError(f'Invalid value for area: {value}')
        self._area = value
        self._side = self._area ** 0.5
        self._perimeter = self._side * 4
        self._diagonal = self._side * (2 ** 0.5)

    @property
    def diagonal(self):
        return f'{self._diagonal:.2f}'

    @diagonal.setter
    def diagonal(self, value):
        if type(value) not in [int, float]:
            raise TypeError(f'Invalid value for diagonal: {value}')
        if value < 0:
            raise ValueError(f'Invalid value for diagonal: {value}')
        self._diagonal = value
        self._side = self._diagonal / (2 ** 0.5)
        self._perimeter = self._side * 4
        self._area = self._side ** 2
