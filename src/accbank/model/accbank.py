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
        self._type = ''

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
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: int):
        """
        This method is special because it looks for the right
        account type available.
        - Payment -> 1
        - Checking -> 2
        - Saving -> 3
        :param type: int. The key to choose.
        :return: None.
        """
        if type < 1 or type > 3:
            return None
        bank = ('Payment', 'Checking', 'Saving')
        self._type = bank[type]

    @property
    def id_acc(self) -> int:
        return self._id_acc

    @id_acc.setter
    def id_acc(self, id_acc: int):
        self._id_acc = id_acc
