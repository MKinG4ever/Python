import random

from Data import *  # random, time, delay, alpha, rgba, random_point
import turtle


def main():
    """Main Part of ModernArt Gallery (v0.1.0)"""
    # TEST PROGRAM
    a = ModernArt(900, 600)
    a.help()
    a.draw_bubbles(25)
    a.draw_liner_dots(100, 5)
    a.draw_exitonclick()


class ModernArt:
    def __init__(self, width: int, height: int):
        self.version = "0.1.2"
        f"""
            Initialize the Modern-Art Project
            author: MKinG
            version: {self.version}
            time: 1715070582.8347054
            :param width: Width of screen in px
            :param height: Height of screen in px
        """
        # Width & Height for set Screen
        self.width = width
        self.height = height
        self.bgcolor = rgba(0.450, 0.450, 0.450)
        # Some turtle Attributes
        self.attr = {
            # turtle
            "speed": 0,
            "color": rgba(),
            # pen
            "pensize": 1,
            "pencolor": rgba(),
            # fill
            "fillcolor": rgba(r=0, g=0, b=0.5),
        }
        # SCREEN and TURTLE Object | Must be created after width, height and attr
        self._screen = self.__screen
        self._turtle = self.__turtle

    def __repr__(self):
        """Return representation of ModernArt"""
        return f"ModernArt v{self.version} | {id(self)}"

    @property
    def __screen(self):
        """Set and setup Screen object"""
        sc = turtle.Screen()
        sc.setup(self.width, self.height, -1, -1)  # set Width and Height
        sc.bgcolor(*self.bgcolor)  # set Background-Color
        return sc

    @property
    def __turtle(self):
        """Set and setup Turtle object"""
        tr = turtle.Turtle()
        # turtle
        tr.hideturtle()  # hide the Turtle
        tr.shape()
        tr.speed(self.attr["speed"])  # set Turtle Speed
        tr.color(*self.attr["color"])  # set Turtle Color
        # pen
        tr.pensize(self.attr["pensize"])  # set pen-size
        tr.pencolor(*self.attr["pencolor"])  # set pen-color
        return tr

    def random_style(self) -> None:
        """Random style for the Turtle object"""
        # feature: wizard to crate more specific style
        t = self._turtle
        # turtle
        t.speed(self.attr["speed"])
        t.color(*self.attr["color"])
        # pen
        t.pensize(round(random.random() * 10 * 3.1415926535))  # random pen-size
        t.pencolor(*rgba(r=0))  # random pen-color
        # fill
        t.fillcolor(*rgba(b=1))  # random fillcolor

    def draw_bubbles(self, bubbles: int) -> None:
        """Draw bubbles on screen in random order"""
        # Materials
        t = self._turtle
        w, h = self.width // 2, self.height // 2
        # Draw
        for i in range(bubbles):
            # size of bubbles
            # color of bubbles
            # check position base on size
            t.teleport(w * random_point(), h * random_point())
            t.pencolor(*rgba(r=0, b=1))  # random pen-color
            t.fillcolor(*rgba(r=0, g=0))  # random fillcolor
            t.begin_fill()
            t.circle(75 * random.random())
            t.end_fill()

    def draw_liner_dots(self, steps: int, loops=1, center_base=True) -> None:
        """Draw sorted circles on screen with random styles"""
        # Materials
        t = self._turtle
        w, h = self.width // 2, self.height // 2
        # Setup new attributes
        t.hideturtle()  # Hide the Turtle
        for loop in range(loops):
            for y in range(-1 * h + steps, h, steps):
                y *= -1
                for x in range(-1 * w + steps, w, steps):
                    rr = random.random() * 35  # random radius | b= base size
                    if center_base:
                        t.teleport(x, y - rr)  # Center Base Circles
                    else:
                        t.teleport(x, y)  # BottomBorder Base Circles [Original CODE]
                    self.random_style()
                    t.circle(rr)

    def draw_exitonclick(self):
        """Exit from ModernArt by click"""
        self._screen.exitonclick()

    def help(self):
        """Basic help() function for ModernArt"""
        print(self.__repr__())
        print("ModernArt:")
        print("\t.random_style()")
        print("\t.draw_bubbles")
        print("\t.draw_liner_dots")
        print("\t.draw_exitonclick")


if __name__ == "__main__":
    main()
