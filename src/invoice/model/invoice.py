from decimal import Decimal
from core.date.date import Date


class Invoice:
    """
    Class Invoice Model.
    """

    def __init__(self):
        """
        New Invoice.
        """
        self._id_card = 0
        self._description = ''
        self._total = Decimal('0.00')
        self._installments = 0
        self._num_installments = 0
        self._value_pay = Decimal('0.00')
        self._finished = False
        self._dateopp = Date()

    @property
    def id_card(self) -> int:
        return self._id_card

    @id_card.setter
    def id_card(self, id_card: int):
        self._id_card = id_card

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def total(self) -> Decimal:
        return self._total

    @total.setter
    def total(self, total: Decimal):
        self._total = total

    @property
    def installments(self) -> int:
        return self._installments

    @installments.setter
    def installments(self, installments: int):
        self._installments = installments

    @property
    def num_installments(self) -> int:
        return self._num_installments

    @num_installments.setter
    def num_installments(self, num_installments: int):
        self._num_installments = num_installments

    @property
    def value_pay(self) -> Decimal:
        return self._value_pay

    @value_pay.setter
    def value_pay(self, value_pay: Decimal):
        self._value_pay = value_pay

    @property
    def finished(self) -> bool:
        return self._finished

    @finished.setter
    def finished(self, finished: bool):
        self._finished = finished

    @property
    def dateopp(self) -> Date:
        return self._dateopp

    @dateopp.setter
    def dateopp(self, dateopp: Date):
        self._dateopp = dateopp
