from decimal import Decimal
from stockholm import Money

class Tax:
    """A tax class.
    """

    def __init__(self, name: str, entity: str, rate: Decimal,  account: str):
        self.name = name
        self.entity = entity
        self.rate = Money(rate)
        self.account = account

    def __repr__(self):
        return 'Tax("%s", "%s")' % (self.name, self.rate)

    def __mul__(self, p2):
        return self.rate * p2
