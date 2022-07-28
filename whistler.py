import os
import time
from datetime import datetime as dt
from random import random as rnd


def delay(sec: int or float) -> None:
    """make an interrupt"""
    time.sleep(sec)


def hr(shape: str = '_', repeat: int = 85) -> None:
    """copy of hr tag from html"""
    count = int(repeat)
    if shape != '':
        shape = str(shape)
        print(shape * repeat)
    else:
        hr('_', count)


def get_time() -> str:
    """
    short-hand for show time or date or time-and-date
    """
    d = dt.today().date()  # Year Month Week Day
    t = dt.today().time()  # Hour Minutes Second Microsecond
    now = f'{str(t)} | {str(d)}'
    return now
    # print(f'Time: {t.hour}:{t.minute}:{t.second} {t.microsecond} \t [{t.max}]')
    # print(f'Date: {d.year}/{d.month}/{d.day} \t Week: {d.weekday()} \t [{d.max}]')


def randal(a, b):
    """inner random function to clear about that"""
    return a + ((b - a) * rnd())


def info(system_command=None) -> None:
    """
    some information about direct folder and related files
    """
    if system_command is not None:
        os.system(system_command)
    path = os.getcwd()
    print(f'path:\t{path}')
