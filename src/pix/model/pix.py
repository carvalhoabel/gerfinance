from decimal import Decimal


class Pix:
    """
    Class Pix.
    """

    def __init__(self):
        """
        New Pix Opp.
        """
        self._send_pix = False
        self._description = ''
        self._id_pixkey = 0
        self._value = Decimal('0.00')

    @property
    def send_pix(self) -> bool:
        return self._send_pix

    @send_pix.setter
    def send_pix(self, send_pix: bool):
        self._send_pix = send_pix

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def id_pixkey(self) -> int:
        return self._id_pixkey

    @id_pixkey.setter
    def id_pixkey(self, id_pixkey: int):
        self._id_pixkey = id_pixkey

    @property
    def value(self) -> Decimal:
        return self._value

    @value.setter
    def value(self, value: Decimal):
        self._value = value
