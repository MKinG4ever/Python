from time import sleep as dly
from random import random as rnd


class Type:
    """
    Type, Echo, Write, Print...
    this module has very names
    by NighFox Type©® beta version 1.2
    open-source release
    """

    def __init__(self, string: str):
        self.string = str(string)
        self.length = len(self.string)
        self.time = lambda: dly(rnd())

    def timer(self, secs: float or int) -> None:
        """set a new setting for time by secs"""
        self.time = lambda: dly((secs / self.length) * rnd())

    def type(self) -> None:
        """Default Type version"""
        for char in self.string:
            print(char, end='')
            self.time()
        if not self.string.endswith('\n'):  # leave a white-line at the end
            print()

    def echo(self) -> None:
        """For devices with low frequency"""
        lines = self.string.split('\n')
        for line in lines:
            ch = str()
            for char in line:
                ch += char
                print(f'\r{ch}', end='')
                self.time()
        if not self.string.endswith('\n'):  # leave a white-line at the end
            print()
