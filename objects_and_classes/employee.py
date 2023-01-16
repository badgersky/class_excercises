class Employee:

    def __init__(self, employee_id, name, surname):
        self.employee_id = employee_id
        self.surname = surname
        self.name = name
        self._salary = 0.0

    def set_salary(self, amount):
        try:
            if amount < 0.0:
                raise ValueError(f'Invalid amount: {amount}')
            else:
                self._salary = float(amount)
        except TypeError:
            raise TypeError(f'Invalid amount: {amount}')

    def __str__(self):
        return f'id: {self.employee_id}, name: {self.name}, surname: {self.surname}'
