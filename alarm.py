import pyttsx3 as tts
import time
import os
import sys


def main():
    print(f'Set your alarm.')
    h, m, s = ask_time()
    alarm(hour=int(h), minute=int(m), second=int(s))


def delay(sec=1):
    time.sleep(sec)


def alarm(hour=0, minute=0, second=0):
    ttf = time_text_format
    t = hour_to_second(hour) + minute_to_second(minute) + second
    for i in range(t):
        p = f'{i / t * 100}'
        print(f'\r[RUNNING: {ttf(i):8} - Remind: {ttf(t - i):8}] [Time: {ttf(t):8}]\t | {p:.5}%', end='')
        delay()
    tts.speak('Ding Ding Ding. Time is up.')


def hour_to_second(hour: int) -> int:
    if hour > 0 and isinstance(hour, int):
        return hour * 60 * 60
    else:
        return 0


def minute_to_second(minute: int) -> int:
    if minute > 0 and isinstance(minute, int):
        return minute * 60
    else:
        return 0


def second_to_time(second: int) -> list:
    s = m = h = int()
    if second >= 60:
        m = second // 60
        s = second % 60
    else:
        s = second
    if m >= 60:
        h = m // 60
        m = m % 60
    return [h, m, s]  # as [Hour, Minute, Second]


def time_text_format(second):
    h, m, s = second_to_time(second)
    return f'{str(h)}:{str(m).zfill(2)}:{str(s).zfill(2)}'


def get_time(hour=0, minute=0, second=0):
    """Convert nonsense times like "101 second" to standard hh/mm/ss"""
    h = hour_to_second(hour)
    m = minute_to_second(minute)
    s = h + m + second  # time base seconds
    t = second_to_time(s)  # time base HH:MM:SS format
    return s, t, '{}:{}:{}'.format(*t)  # seconds, second_to_time, time format


def ask_time():
    h, m, s = input('Enter time as HH:MM:SS Format: ').strip().split(':')
    return h, m, s


if __name__ == '__main__':
    main()
