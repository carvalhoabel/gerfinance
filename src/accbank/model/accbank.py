from core.utils.banks import BankGeneral


class AccBank(BankGeneral):
    """
    New Bank Account.
    """

    def __init__(self):
        """
        New Bank Account.
        """
        super().__init__()
        self._agency = self._number = self._id_acc = 0

    @property
    def agency(self) -> int:
        return self._agency

    @agency.setter
    def agency(self, agency: int):
        self._agency = agency

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number

    @property
    def id_acc(self) -> int:
        return self._id_acc

    @id_acc.setter
    def id_acc(self, id_acc: int):
        self._id_acc = id_acc
