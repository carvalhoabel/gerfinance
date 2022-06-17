from decimal import Decimal


class Saving:
    """
    Saving Account Class.
    """

    def __init__(self):
        """
        New Saving Account.
        """
        self._id_bank = self._variation = 0
        self._balance = Decimal('0.00')

    @property
    def id_bank(self) -> int:
        return self._id_bank

    @id_bank.setter
    def id_bank(self, id_bank: int):
        self._id_bank = id_bank

    @property
    def variation(self) -> int:
        return self._variation

    @variation.setter
    def variation(self, variation: int):
        self._variation = variation

    @property
    def balance(self) -> Decimal:
        return self._balance

    @balance.setter
    def balance(self, balance: Decimal):
        self._balance = balance
