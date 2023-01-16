class Shape:

    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def describe(self):
        message = f'{self.color.title()} colored shape has its center in point{self.x, self.y}.'
        print(message)

    def distance(self, other_shape):
        x, y = other_shape.x, other_shape.y
        distance = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return distance

    def __str__(self):
        return f'Shape color: {self.color}, center point: {self.x, self.y}'


shape1 = Shape(10, 10, 'green')
shape2 = Shape(5, 5, 'blue')

shape1.describe()
shape2.describe()
print(shape1)
print(shape2)
print(shape1.distance(shape2))
print(shape2.distance(shape1))
