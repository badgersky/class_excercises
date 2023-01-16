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

    def show_operations(self):
        for operation in self.operation_list:
            print(operation)


calc1 = Calculator()

print(calc1.add(30, 39))
print(calc1.add(400, 20))
calc1.show_operations()
print(calc1.multiply(2, 2))
print(calc1.multiply(30, 2))
calc1.show_operations()
