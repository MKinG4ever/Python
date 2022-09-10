import os
import platform
import random
import sys
import time
import math
import string
from datetime import datetime

"""
Sample of how works a ransomware
"""


def dly():
    time.sleep(random.random() / math.pi)


# Gathering data
_UserName = os.getlogin()
_ExactMoment = time.time()
_TimeStamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
_Directory = os.getcwd()
_ScanDir = os.listdir(_Directory)
_Node = platform.node()
_SystemOS = platform.system()
_Machine = platform.machine()
_Core = platform.processor()
_cpuCores = os.cpu_count()
_Drives = [f'{i}:\\' for i in string.ascii_uppercase if os.path.isdir(f'{i}:\\')]
_Root = f'{_Directory[0]}:\\' if os.path.isdir(f'{_Directory[0]}:\\') else None
_PersonalFiles = [f'{d}Users\\{_UserName}' for d in _Drives if os.path.isdir(f'{d}Users\\{_UserName}')]
_pid = os.getpid()
_ppid = os.getppid()

for _ in 'Gathering data...\n':
    print(f'{_}', end='')
    dly()

data = {
    '_UserName': _UserName,
    '_TimeStamp': _TimeStamp,
    '_ExactMoment': _ExactMoment,
    '_Directory': _Directory,
    '_ScanDir': _ScanDir,
    '_Root': _Root,
    '_Node': _Node,
    '_SystemOS': _SystemOS,
    '_Machine': _Machine,
    '_Core': _Core,
    '_cpuCores': _cpuCores,
    '_Drives': _Drives,
    '_PersonalFiles': _PersonalFiles,
    '_ppid': _ppid,
    '_pid': _pid
}

with open('data.txt', 'w') as file:
    for k, v in data.items():
        blue_print = f'{k:16}:\t{v}'
        file.write(blue_print + '\n')
        print(blue_print)
        dly()

for _ in 'Done.\n':
    print(_, end='')
    dly()

if input('Enter the safeguard password:') != 'secure':
    print('\033[91m')
    for _ in '-Safeguard password is Wrong!':
        print(_, end='')
        time.sleep(random.random())
        quit()
        sys.exit()  # make sure program end here

with open('log.txt', 'w') as log:
    for drive in _Drives[:1]:
        print(f'Scan( {drive} )')
        time.sleep(1)
        for root, dirs, files in os.walk(drive):
            try:
                log.write(f'\n{root}\n{dirs}\n{files}\n')
            except Exception as exp:
                log.write(f'\nSOME ERROR COMING\n')
                print('Some Error.')

print('Program is End.\n')
