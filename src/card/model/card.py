from decimal import Decimal
from core.date.date import Date


class Card:
    """
    Card Class.
    """

    def __init__(self):
        """
        New Card.
        """
        self._number = ''
        self._valid = Date()
        self._id_bank = 0
        self._flag = ''
        self._limit = Decimal('0.00')
        self._type_card = ''

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

    @property
    def valid(self) -> Date:
        return self._valid

    @valid.setter
    def valid(self, valid: Date):
        self._valid = valid

    @property
    def id_bank(self) -> int:
        return self._id_bank

    @id_bank.setter
    def id_bank(self, id_bank: int):
        self._id_bank = id_bank

    @property
    def flag(self) -> str:
        return self._flag

    @flag.setter
    def flag(self, flag: str):
        self._flag = flag

    @property
    def limit(self) -> Decimal:
        return self._limit

    @limit.setter
    def limit(self, limit: Decimal):
        self._limit = limit

    @property
    def type_card(self) -> str:
        return self._type_card

    @type_card.setter
    def type_card(self, type_card: int):
        """
        This method chose between Prepaid and Credit/Debit.

        - pre paid -> 1
        - credit/debit 2

        :param type_card: int. the access key.
        :return: None.
        """
        if 0 < type_card < 3:
            cards = ('Pre-Paid', 'Credit/Debit')
            self._type_card = cards[type_card]
