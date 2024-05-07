from random import random as rnd
import random
import turtle
import time


def main():
    """Main Part of ModernArt Gallery (v0.1.0)"""
    # TEST PROGRAM
    m = ModernArt(1000, 1200)
    m.draw_bubbles(25)
    m.draw_liner_dots(100, 50)


# Static functions
def delay(sec=None) -> None:
    """Manual interrupt function"""
    if sec is None:
        # sec == None
        time.sleep((rnd() * 3.14159265358979) + 0.01)  # interrupt for 0.01 ~ 3.14 seconds
    elif isinstance(float(sec), float):
        # sec == float()
        time.sleep(float(sec))  # interrupt as "sec"


def rgba(r=None, g=None, b=None) -> tuple:
    """Returns  a tuple(red, green, blue) as random color"""
    # feature: set a constance value for 'r','g' or 'b' parameters
    return float(f"{rnd():.3}"), float(f"{rnd():.3}"), float(f"{rnd():.3}")  # [Output] rnd() : 0.000 ~ 1.000


# the ModernArt Gallery Class
class ModernArt:
    def __init__(self, width, height):
        """
            Initialize the Modern-Art Project
            author: MKinG
            version: 0.1.0
            time: 1715070582.8347054
        """
        # Width & Height for set Screen
        self.width = width
        self.height = height
        # Some turtle Attributes
        self.attr = {
            "speed": 0,
            "color": rgba(),
            "pensize": 1,
            "pencolor": rgba(),
            "fillcolor": rgba(),
        }
        # SCREEN and TURTLE Object | Must be created after width, height and attr
        self._screen = self.__screen
        self._turtle = self.__turtle

    def __repr__(self):
        """Return representation of ModernArt"""
        return f"ModernArt v0.1 | {print(id(self))}"

    @staticmethod
    def random_point() -> float:
        """Return a number between -1 and +1"""
        return rnd() * random.choice([1, -1])

    @property
    def __screen(self):
        """Set and setup Screen object"""
        sc = turtle.Screen()
        sc.setup(self.width, self.height, 0, 0)  # set Width and Height
        sc.bgcolor((0.750, 0.750, 0.750))  # set Background-Color
        return sc

    @property
    def __turtle(self):
        """Set and setup Turtle object"""
        tr = turtle.Turtle()
        tr.speed(self.attr["speed"])  # set Turtle Speed
        tr.color(self.attr["color"])  # set Turtle Color
        tr.pensize(self.attr["pensize"])  # set pen-size
        tr.pencolor(self.attr["pencolor"])  # set pen-color
        return tr

    def random_style(self) -> None:
        """Random style for the Turtle object"""
        # turtle visibility
        # turtle shape
        # turtle color
        # turtle speed
        # pencolor
        # pensize
        # fill or Not fill
        # fillcolor
        t = self._turtle
        t.pensize(round(rnd() * 10 * 3.1415926535))  # random pen-size
        t.pencolor(rgba())  # random pen-color
        t.fillcolor(rgba())  # random fillcolor

    def draw_bubbles(self, bubbles: int) -> None:
        """Draw bubbles on screen in random order"""
        # Materials
        t = self._turtle
        w, h = self.width // 2, self.height // 2
        # Setup new attributes
        # t.hideturtle()  # Hide the Turtle
        # Draw
        for i in range(bubbles):
            # size of bubbles
            # color of bubbles
            # check position base on size
            t.teleport(w * self.random_point(), h * self.random_point())
            self.random_style()
            t.begin_fill()
            t.circle(75 * rnd())
            t.end_fill()

    def draw_liner_dots(self, steps: int, loops=1) -> None:
        # Materials
        t = self._turtle
        w, h = self.width // 2, self.height // 2
        # Setup new attributes
        # t.hideturtle()  # Hide the Turtle
        for loop in range(loops):
            for y in range(-1 * h + steps, h, steps):
                y *= -1
                for x in range(-1 * w + steps, w, steps):
                    rr = rnd() * 35  # random radius | b= base size
                    # t.teleport(x, y)  # BottomBorder Base Circles [Original CODE]
                    t.teleport(x, y - rr)  # Center Base Circles
                    self.random_style()
                    t.circle(rr)


if __name__ == "__main__":
    main()
