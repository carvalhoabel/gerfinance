from core.date.date import Date


class Account:
    """
    New Account Class.
    """

    def __init__(self):
        """
        New Account Instance.
        """
        self._fullname = self._cpf = self._email = ''
        self._username = self._passwd = self._mobile = ''
        self._birthday = Date()

    @property
    def fullname(self) -> str:
        return self._fullname

    @fullname.setter
    def fullname(self, fullname: str):
        self._fullname = fullname

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self._cpf = cpf

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str):
        self._username = username

    @property
    def passwd(self) -> str:
        return self._passwd

    @passwd.setter
    def passwd(self, passwd: str):
        self._passwd = passwd

    @property
    def mobile(self) -> str:
        return self._mobile

    @mobile.setter
    def mobile(self, mobile: str):
        self._mobile = mobile

    @property
    def birthday(self) -> Date:
        return self._birthday
