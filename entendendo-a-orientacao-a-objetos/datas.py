""" Class creation challenge"""


class Data:
    """define Data"""

    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def formatada(self):
        """Return fomated date"""
        print("{}/{}/{}".format(self.day, self.month, self.year))
