from decimal import Decimal


class Payment:
    """
    Payment Account Class.
    """

    def __init__(self):
        """
        New Payment Account.
        """
        self._id_bank = 0
        self._balance = Decimal('0.00')
        self._save = Decimal('0.00')

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

    @property
    def save(self) -> Decimal:
        return self._save

    @save.setter
    def save(self, save: Decimal):
        self._save = save
