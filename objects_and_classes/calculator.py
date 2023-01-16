class Calculator:

    def __init__(self):
        self.operation_list = []

    def add(self, num1, num2):
        result = num1 + num2
        self.operation_list.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.operation_list.append(f'multiplied {num1} with {num2} got {result}')
        return result
    