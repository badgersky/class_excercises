class Book:

    def __init__(self, title, author, isbn):
        self.isbn = isbn
        self.author = author
        self.title = title
        if not self.check_isbn(isbn):
            raise ValueError(f'Invalid isbn number: {isbn}')

    @staticmethod
    def check_isbn(n):
        while '-' in n:
            n = n.replace('-', '')
        n = n[::-1]
        control_num = n[0]
        n = n.replace(control_num, '', 1)
        n = n[::-1]
        control_num = int(control_num)

        if len(n) == 9:
            control_mul = [i * int(num) for i, num in enumerate(n, start=1)]
            control_sum = sum(control_mul)
            if control_sum % 11 == control_num:
                return True
        elif len(n) == 12:
            control_mul = [1 * int(num) if i % 2 == 0 else 3 * int(num) for i, num in enumerate(n)]
            control_sum = sum(control_mul)
            if control_sum % 10 == 0 == control_num:
                return True
            else:
                rest = control_sum % 10
                if 10 - rest == control_num:
                    return True
        return False
