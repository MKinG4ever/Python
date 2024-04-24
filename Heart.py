import math
import turtle


def main():
    art = """No matter what is the question, When LOVE is the answer...
    
      ,d88b.d88b,
      88888888888
      `Y8888888Y'
        `Y888Y'
          `Y'
    """

    t = turtle
    t.speed(0)
    t.bgcolor('black')

    try:
        for i in range(6000):
            t.goto(heart_a(i) * 20, heart_b(i) * 20)

            for j in range(5):
                t.color("#f73487")

            t.goto(0, 0)
        t.done()
    except Exception as e:
        print(f"{art}\nError: \n{e}")
        sys.exit(0)


def heart_a(k):
    return 15 * math.sin(k) ** 3


def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


if __name__ == '__main__':
    main()
