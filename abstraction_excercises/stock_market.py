import random


class CommandPrompt:

    def __init__(self):
        self.wait = ('', 'w', 'wait')
        self.sell = ('s', 'sell')
        self.buy = ('b', 'buy')
        self.correct_answers = self.wait + self.sell + self.buy

    def ask(self):
        while True:
            choice = input(f'Decision [b/s/w/buy/sell/wait/""]: ')
            if choice not in self.correct_answers:
                print(f'Wrong choice: {choice}')
            else:
                break
        if choice in self.buy:
            return 'buy'
        if choice in self.sell:
            return 'sell'
        return 'wait'


class Wallet:

    def __init__(self, pln, usd):
        self.usd = usd
        self.pln = pln

    def convert_pln_to_usd(self, usdpln_rate):
        if self.pln:
            self.usd = self.pln / usdpln_rate
            self.pln = 0.0
            return self.usd, self.pln
        return self.usd, self.pln

    def convert_usd_to_pln(self, usdpln_rate):
        if self.usd:
            self.pln = self.usd * usdpln_rate
            self.usd = 0.0
            return self.usd, self.pln
        return self.usd, self.pln


stock_question = CommandPrompt()

random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0
    wallet = Wallet(wallet_pln, wallet_usd)
    for usdpln_rate in usdpln_rates:
        print(f'Account balance: {round(wallet_pln, 2)}zł, ${round(wallet_usd, 2)}, exchange rate {usdpln_rate}')
        choice = stock_question.ask()
        if choice == 'buy':
            wallet_usd, wallet_pln = wallet.convert_pln_to_usd(usdpln_rate)
        elif choice == 'sell':
            wallet_usd, wallet_pln = wallet.convert_usd_to_pln(usdpln_rate)

    wallet_pln = wallet.convert_usd_to_pln(usdpln_rate)[1]
    print(f'Your score: {wallet_pln}zł!')


if __name__ == '__main__':
    main(random_usdpln_rates)
