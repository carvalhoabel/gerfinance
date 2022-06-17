class Pixkey:
    """
    Pixkey Class.
    """

    def __init__(self):
        self._id_accbank = 0
        self._keypix = self._type_key = ''

    @property
    def id_accbank(self) -> int:
        return self._id_accbank

    @id_accbank.setter
    def id_accbank(self, id_accbank: int):
        self._id_accbank = id_accbank

    @property
    def keypix(self) -> str:
        return self._keypix

    @keypix.setter
    def keypix(self, keypix: str):
        self._keypix = keypix

    @property
    def type_key(self) -> str:
        return self._type_key

    @type_key.setter
    def type_key(self, type_key: int):
        """
        This method select the pix key type.

        - email -> 1
        - mobile -> 2
        - cpf/cnpj -> 3
        - random -> 4

        :param type_key: int. The access key.
        :return: None.
        """
        if not 0 < type_key < 5:
            types_pix = ('email', 'mobile', 'cpf/cnpj', 'random')
            self._type_key = types_pix[type_key-1]
