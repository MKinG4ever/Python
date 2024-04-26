import random as rnd
from time import sleep as dly
import pprint as pp

color_format_1 = "\x1b[6;30;42m"  # \x1b[ (0..100;0..100;0..100) m
color_format_2 = "\033[99m"  # \033[ (0..108) m

# single value
for i in range(107):
    print(f"\033[{i}m" + f"[{i:3}]\t" + " - Hello World!")

# three value
"""
for i in range(107):
    for j in range(107):
        for k in range(107):
            color = f"\x1b[{i};{j};{k}m"
            print(color + f"{i, j, k}")
"""
