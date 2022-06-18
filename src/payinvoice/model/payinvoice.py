from decimal import Decimal


class PayInvoice:
    """
    PayInvoice Model Class.
    """

    def __init__(self):
        """
        New Payment Invoice.
        """
        self._id_invoice = 0
        self._total = Decimal('0.00')
        self._percent = Decimal('0.00')
        self._total_paid = Decimal('0.00')
        self._description = ''

    @property
    def id_invoice(self) -> int:
        return self._id_invoice

    @id_invoice.setter
    def id_invoice(self, id_invoice: int):
        self._id_invoice = id_invoice

    @property
    def total(self) -> Decimal:
        return self._total

    @total.setter
    def total(self, total: Decimal):
        self._total = total

    @property
    def percent(self) -> Decimal:
        return self._percent

    @percent.setter
    def percent(self, percent: Decimal):
        self._percent = percent

    @property
    def total_paid(self) -> Decimal:
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid: Decimal):
        self._total_paid = total_paid

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description
