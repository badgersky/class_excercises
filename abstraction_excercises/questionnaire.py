class SingleChoiceQuestion:

    def __init__(self, question, answers):
        self.answers = answers
        self.question = question

    def ask(self):
        print(f'\n{self.question}')
        for number, answer in enumerate(self.answers, start=97):
            print(f'{chr(number)}) {answer}')
        while True:
            choice = input('Your answer: ')
            if ord(choice) not in range(97, len(self.answers) + 97):
                print('Wrong answer, try again.')
            else:
                return choice


class Questionnaire:

    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(f'{self.title}')
        result = {}
        for number, question in enumerate(self.questions):
            answer = question.ask()
            result[number] = answer
        print('\nThank You!')
        return result


# questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
# q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
# q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
# q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
# questionnaire.add_question(q1)
# questionnaire.add_question(q2)
# questionnaire.add_question(q3)
# answers = questionnaire.run()
# print(answers)


