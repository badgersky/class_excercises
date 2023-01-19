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
        print(type(a))
        print(type(b))
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


calc = Calculator()
print(calc.mul(2, 'eh'))
