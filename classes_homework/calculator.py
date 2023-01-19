class Calculator:

    @staticmethod
    def add(a, b):
        try:
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
            return a * b
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
        