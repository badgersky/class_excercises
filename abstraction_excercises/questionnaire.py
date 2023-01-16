class SingleChoiceQuestion:

    def __init__(self, question, answers):
        self.answers = answers
        self.question = question

    def ask(self):
        print(self.question)
        for number, answer in enumerate(self.answers, start=97):
            print(f'{chr(number)}) {answer}')
        while True:
            choice = input('Your answer: ')
            if ord(choice) not in range(97, len(self.answers) + 97):
                print('Wrong answer, try again.')
            else:
                return choice



