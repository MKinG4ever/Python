from random import random as rnd
from time import sleep as dly
import os, sys, platform, time

"""
soft way to just take a quick look at the model methods.
it's powered by dir() built-in function
try 'os', 'sys', 'platform' or 'time' for example
but you can import another modules and check them too
"""

ex = ['abort', 'close', 'exit', 'break', 'kill', 'breakpointhook', '__breakpointhook__']


def delay():
    dly(rnd() / 3.14159265)


def show(module: str, *args) -> None:
    counter = 0
    n = str(module)  # str(random)
    m = eval(n)  # eval(str(random))
    d = dir(m)  # dir(eval(str(random)))

    for o in d:
        counter += 1
        s = n + '.' + o
        print(f'({str(counter).zfill(3):3}/{len(d)}) \t {n}.\"{o}\"')
        if o in ex:  # breaker modules
            print()
            continue
        e = eval(s)
        print(e, f'[{type(e)}]')
        if not isinstance(e, str) and not isinstance(e, int):
            try:
                print(eval(f'{s}()'))
            except Exception:
                print('\033[91mArgument Error...\033[0m')
            finally:
                print()
                delay()
        else:
            print()
            delay()
