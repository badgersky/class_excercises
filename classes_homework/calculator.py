class Calculator:

    @staticmethod
    def add(a, b):
        try:
            if type(a) not in [int, float] and type(b) not in [int, float]:
                raise TypeError
            return a + b
        except TypeError:
            return f'Invalid arguments'

    @staticmethod
    def sub(a, b):
        try:
            return a - b
        except TypeError:
            return f'Invalid arguments'

    @staticmethod
    def mul(a, b):
        try:
            if type(a) in [int, float] and type(b) in [int, float]:
                return a * b
            else:
                raise TypeError
        except TypeError:
            return f'Invalid arguments'

    @staticmethod
    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return f'You cannot divide by 0'
        except TypeError:
            return f'Invalid arguments'


class LoggingCalculator(Calculator):

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self.history.append(f'{a} + {b} = {result}')
        return result

    def mul(self, a, b):
        result = super().mul(a, b)
        self.history.append(f'{a} * {b} = {result}')
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        self.history.append(f'{a} - {b} = {result}')
        return result

    def div(self, a, b):
        result = super().div(a, b)
        self.history.append(f'{a} / {b} = {result}')
        return result


calc = LoggingCalculator()
print(calc.add(2, 3))
print(calc.mul(3, 3))
print(calc.sub(7, 4))
print(calc.div(5, 2))
print(calc.history)



