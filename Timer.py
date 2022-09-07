from functools import wraps
import time


def timing(func):
    """Timing functions for methods"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Timing: {finish_time - start_time}')
        return result

    return wrapper()