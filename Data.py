import random
import time


# Static functions
def delay(sec=None) -> None:
    """
        Interrupt function base of input, manual or random.
        :param sec: Time in seconds to interrupt
    """
    if sec is None:
        # sec == None
        time.sleep((random.random() * 3.14159265358979) + 0.01)  # interrupt for 0.01 ~ 3.14 seconds
    elif isinstance(float(sec), float):
        # sec == float()
        time.sleep(float(sec))  # interrupt as "sec"


def alpha(number=None) -> float:
    """
        Manual or Random number, for rgba() function.
        :param number: a number between 0 and 1
    """
    if number is None:
        return random.random()  # [Output] rnd() : 0.000 ~ 1.000
    else:
        return float(number)  # 1 -> 1.000


def rgba(r=None, g=None, b=None) -> tuple:
    """
        Returns a tuple(red, green, blue) that contains semi-random numbers.
        :param r: Red: float between 0 and 1
        :param g: Green: float between 0 and 1
        :param b: Blue: float between 0 and 1
    """
    # feature: from a-b range for r,g,b
    return alpha(r), alpha(g), alpha(b)


def random_point() -> float:
    """Return a number between -1 and +1"""
    return random.random() * random.choice([1, -1])
