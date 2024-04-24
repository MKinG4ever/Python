import random as rnd
import string as strs


def rnd_py_pass_gen():
    """random passphrase generator by python"""
    let = strs.ascii_letters
    num = strs.digits
    sym = strs.punctuation
    # input
    pattern = input('Enter number of letters, numbers and symbols in order(separate with space). like: 5 3 4 ')
    _l, _n, _s, *_others = pattern.strip().split(' ')
    # pieces
    _l = [rnd.choice(let) for _ in range(int(_l))]
    _n = [rnd.choice(num) for _ in range(int(_n))]
    _s = [rnd.choice(sym) for _ in range(int(_s))]
    # shuffle variables
    _p = _l + _n + _s
    rnd.shuffle(_p)

    return ''.join(_p)
  
