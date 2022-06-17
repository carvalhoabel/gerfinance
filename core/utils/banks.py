from typing import Generator
from abc import ABCMeta


def banks_brazil() -> Generator:
    all_banks_brazil = (
        (
            ('officialname', 'Banco ABC Brasil S.A.'),
            ('knowas', 'Banco ABC Brasil'),
            ('code', '246'),
        ),
        (
            ('officialname', 'Banco ABN Amro S.A.'),
            ('knowas', 'Banco ABN Amro'),
            ('code', '075'),
        ),
        (
            ('officialname', 'Banco Agibank S.A.'),
            ('knowas', 'Agibank'),
            ('code', '121'),
        ),
        (
            ('officialname', 'Banco Alfa S.A.'),
            ('knowas', 'Banco Alfa'),
            ('code', '025'),
        ),
        (
            ('officialname', 'Banco Arbi S.A.'),
            ('knowas', 'Banco Arbi'),
            ('code', '213'),
        ),
        (
            ('officialname', 'Banco B3 S.A.'),
            ('knowas', 'Banco B3'),
            ('code', '096'),
        ),
        (
            ('oficialname', 'Banco Bandepe S.A.'),
            ('knowas', 'Banco Bandepe'),
            ('code', '024'),
        ),
        (
            ('officialname', 'Banco BMG S.A.'),
            ('knowas', 'Banco BMG'),
            ('code', '318'),
        ),
        (
            ('officialname', 'Banco BNP Paribas Brasil S.A.'),
            ('knowas', 'Banco BNP Paribas'),
            ('code', '752'),
        ),
        (
            ('officialname', 'Banco Bocom BBM S.A.'),
            ('knowas', 'Banco Bocom'),
            ('code', '107'),
        ),
        (
            ('officialname', 'Banco Bradesco S.A.'),
            ('knowas', 'Banco Bradesco'),
            ('code', '237'),
        ),
        (
            ('officialname', 'Banco BS2 S.A.'),
            ('knowas', 'Banco BS2'),
            ('code', '218'),
        ),
        (
            ('officialname', 'Banco BTG Pactual S.A.'),
            ('knowas', 'Banco BTG Pactual'),
            ('code', '208'),
        ),
        (
            ('officialname', 'Banco C6 S.A.'),
            ('knowas', 'Banco C6'),
            ('code', '336'),
        ),
        (
            ('officialname', 'Banco Caixa Geral S.A>'),
            ('knowas', 'Banco Caixa Geral'),
            ('code', '473'),
        ),
        (
            ('officialname', 'Banco Cargill S.A.'),
            ('knowas', 'Banco Cargill'),
            ('code', '040'),
        ),
        (
            ('officialname', 'Banco Cifra S.A.'),
            ('knowas', 'Banco Cifra'),
            ('code', '233'),
        ),
        (
            ('officialname', 'Banco Citibank S.A.'),
            ('knowas', 'Citibank'),
            ('code', '754'),
        ),
        (
            ('officialname', 'Banco do Brasil S.A.'),
            ('knowas', 'Banco do Brasil'),
            ('code', '001'),
        ),
        (
            ('officialname', 'Banco Inter S.A.'),
            ('knowas', 'Banco Inter'),
            ('code', '077'),
        ),
        (
            ('officialname', 'Banco ItauBank S.A.'),
            ('knowas', 'Banco Itau'),
            ('code', '479'),
        ),
        (
            ('officialname', 'Banco Safra S.A.'),
            ('knowas', 'Banco Safra'),
            ('code', '422'),
        ),
        (
            ('officialname', 'Banco Original S.A.'),
            ('knowas', 'Banco Original'),
            ('code', '212'),
        ),
        (
            ('officialname', 'Banco Pan S.A.'),
            ('knowas', 'Banco Pan'),
            ('code', '613'),
        ),
        (
            ('officialname', 'Banco Santander S.A.'),
            ('knowas', 'Banco Santander'),
            ('code', '033'),
        ),
        (
            ('officialname', 'Nu Pagamentos S.A.'),
            ('knowas', 'Nubank'),
            ('code', '260'),
        ),
        (
            ('officialname', 'Pagseguro Internet S.A.'),
            ('knowas', 'PagBank'),
            ('code', '290'),
        ),
        (
            ('officialname', 'PicPay Serviços S.A.'),
            ('knowas', 'PicPay'),
            ('code', '380'),
        ),
        (
            ('officialname', 'Mercado Pago S.A.'),
            ('knowas', 'Mercado Pago'),
            ('code', '323'),
        ),
        (
            ('officialname', 'Banco Neon S.A.'),
            ('knowas', 'Neonbank'),
            ('code', '735'),
        )
    )
    for bank in all_banks_brazil:
        yield dict(bank)


class BankGeneral(metaclass=ABCMeta):
    """
    Abstract class to Bank class.
    """

    def __init__(self):
        """
        New Bank.
        """
        self._officialname = self._knowas = ''
        self._code = 0

    @property
    def officialname(self):
        return self._officialname

    @officialname.setter
    def officialname(self, officialname: str):
        self._officialname = officialname

    @property
    def knowas(self):
        return self._knowas

    @knowas.setter
    def knowas(self, knowas: str):
        self._knowas = knowas

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, code: int):
        self._code = code
