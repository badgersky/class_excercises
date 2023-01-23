class Price23Vat:

    def __init__(self, pretax):
        self._pretax = pretax
        self._net = self._pretax / 1.23
        self._tax = self._pretax - self._net

    @property
    def net(self):
        return self._net

    @net.setter
    def net(self, value):
        self._net = value
        self._pretax = self._net * 1.23
        self._tax = self._pretax - self._net

    @property
    def pretax(self):
        return self._pretax

    @pretax.setter
    def pretax(self, value):
        self._pretax = value
        self._net = self._pretax / 1.23
        self._tax = self._pretax - self._net

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._tax = value
        self._net = self._tax / 0.23
        self._pretax = self._net * 1.23
