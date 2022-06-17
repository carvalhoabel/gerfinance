from decimal import Decimal


class Checking:
    """
    Checking Account Class.
    """

    def __init__(self):
        """
        New Checking Account.
        """
        self._id_bank = 0
        self._balance = Decimal('0.00')

    @property
    def id_bank(self) -> int:
        return self._id_bank

    @id_bank.setter
    def id_bank(self, id_bank: int):
        self._id_bank = id_bank

    @property
    def balance(self) -> Decimal:
        return self._balance

    @balance.setter
    def balance(self, balance: Decimal):
        self._balance = balance
