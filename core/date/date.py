class Date:
    """This class represents the date.
    """

    def __init__(self):
        """
        New Date.
        """
        self._month = self._day = self._year = 0

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month: int):
        self._month = month

    @property
    def day(self):
        return self._month

    @day.setter
    def day(self, day: int):
        self._day = day

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year
