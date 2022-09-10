from random import random as rnd
from time import sleep as dly
import os, sys, platform, time
import numpy as np

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


_1 = os.cpu_count()  # 8
_2 = os.environ
_3 = os.getcwd()  # C:\Users\nightfox\Documents\Python
_4 = os.getlogin()  # nightfox
_5 = os.getpid()  # 3004
_6 = os.getppid()  # 8624
_7 = os.kill  # <built-in function kill>
_8 = os.listdir()  # ['.idea', '2000', '2001', '2002', 'ransomware.py', 'main.py', 'module_check.py', 'shorthand.py', 'test.py', 'Timer.py', 'Try.py', 'Type.py', 'whistler.py', '__pycache__']
_9 = os.mkdir  # make a direction (folder)
_10 = os.makedirs  # make a directions
_11 = os.remove  #
_12 = os.removedirs  #
_13 = os.renames  #
_14 = os.rmdir  #
_15 = os.scandir()  # Iterator value
_16 = os.system  # Enter system (cmd/terminal) command
_17 = platform.architecture()  # ('64bit', 'WindowsPE')
_18 = platform.machine()  # AMD64
_19 = platform.node()  # Arora
_20 = platform.platform()  # Windows-10-10.0.22000-SP0
_21 = platform.processor()  # Intel64 Family 6 Model 158 Stepping 13, GenuineIntel
_22 = platform.python_compiler()  # MSC v.1929 64 bit (AMD64)
_23 = platform.python_version()  # 3.10.5
_24 = platform.system()  # Windows (tell your os system)
_25 = platform.uname()  # uname_result(system='Windows', node='Arora', release='10', version='10.0.22000', machine='AMD64')
_26 = platform.win32_edition()  # Professional
_27 = platform.win32_is_iot()  # False
_28 = platform.win32_ver()  # ('10', '10.0.22000', 'SP0', 'Multiprocessor Free')
_29 = sys.argv  # ['C:/Users/nightfox/Documents/Python/ransomware.py'] ,[prefix]
_30 = sys.exit  # be carfull
_31 = sys.getdefaultencoding()  # utf-8
_32 = sys.path  # ['C:\\Users\\nightfox\\Documents\\Python', ...]
_33 = sys.path_importer_cache  # {'C:\\Users\\nightfox\\Documents\\Python': FileFinder('C:\\Users\\nightfox\\Documents\\Python'), ..}
_34 = sys.platform  # win32
_35 = sys.version  # 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]

"""
    for i in range(1, 36):
    a = f'_{i}'
    print(f'[{i}]: ', eval(a), '\n')
"""

x1=np.random.SeedSequence()  # entropy
x2=np.random.permutation(10)
