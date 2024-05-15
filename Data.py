import random


class RGB:
    """
    Represents an RGB color object with features for hexadecimal and RGB types representation.
        Features: create new colors base of one (seed)

    author: MKinG
    time: 1715816023.4784908
    """

    def __init__(self, r=None, g=None, b=None):
        """
        Initialize RGB color object.
        - given argument(s) will override to float
        - None argument(s) will be randomized

        :param r: Red color value (0 to 1), defaults to None
        :param g: Green color value (0 to 1), defaults to None
        :param b: Blue color value (0 to 1), defaults to None
        """
        self.r = self.generator(r)
        self.g = self.generator(g)
        self.b = self.generator(b)

    def __repr__(self):
        """Representation of RGB object."""
        return f"RGB Modules {self.version}\nValue:\n\t{self.rgb}\n\t{self.cir}\n\t{self.hex}"

    def __str__(self):
        """String representation of RGB color."""
        return f"{self.r}, {self.g}, {self.b}"  # Used of original values to return 'str()'

    def __iter__(self):
        """Iterator representation of RGB color."""
        return iter((self.r, self.g, self.b))  # Used of original values to return in list(), tuple() and iter() types

    @staticmethod
    def to_hex(number) -> str:
        """
        Convert a number between 0 and 1 to hexadecimal format.
        - for convert rgb to hex(hexadecimal)

        :param number: Number between 0 and 1
        :return: Hexadecimal representation of the number
        """
        return hex(int(number * 255))[2:].zfill(2)

    @staticmethod
    def to_cir(number) -> int:
        """
         Convert a number to a color value within the circular color space (0 to 255).
        - for convert rgb to cir(circle of color)

        :param number: Number between 0 and 1
        :return: Number in the range of 0 to 255 as int()
        """
        return int(number * 255)

    @staticmethod
    def generator(number=None) -> float:
        """
        Generate a random or specified color value.
        - make sure number is between 0 and 1
        - None input argument will be randomized

        :param number: A number between 0 and 1, defaults to None
        :return: Random color value if None, otherwise returns the input value
        """
        if number is None:
            # if number is None, generate a random number for color
            return random.random()  # Output: 0.000 ~ 1.000
        elif isinstance(float(number), float):
            # if number can be converted to float()
            if number > 1:
                return float(1)  # If number exceeds 1, return the maximum value of 1
            elif number < 0:
                return float(0)  # If number is less than 0, return the minimum value of 0
            else:
                return float(number)  # Ex: 1 -> 1.000

    @property
    def rgb(self) -> tuple:
        """
        Return the current RGB color values in a tuple. (Original Method)
         - floats with only 3 number after point (Ex: 0.123456789 -> 0.123)

        :return: Tuple containing (R, G, B) color values
        """
        r = float("{:.3f}".format(self.r))
        g = float("{:.3f}".format(self.g))
        b = float("{:.3f}".format(self.b))
        return r, g, b

    @property
    def cir(self) -> tuple:
        """
        Get the circular color space representation of the current RGB color values.

        :return: Tuple containing (R, G, B) color values in the range of 0 to 255
        """
        cir_r = self.to_cir(self.r)
        cir_g = self.to_cir(self.g)
        cir_b = self.to_cir(self.b)
        return cir_r, cir_g, cir_b

    @property
    def hex(self) -> str:
        """
        Get the hexadecimal representation of the current RGB color values.

        :return: Hexadecimal representation of the RGB color
        """
        hex_r = self.to_hex(self.r)
        hex_g = self.to_hex(self.g)
        hex_b = self.to_hex(self.b)
        return f"#{hex_r}{hex_g}{hex_b}"

    @property
    def version(self) -> str:
        """
        Get the version of the RGB Modules.

        :return: Version string formatted with three numbers after the decimal point
        """
        return f"0.3.7"

    def random_color(self, r=None, g=None, b=None) -> tuple:
        """
        Generate a random RGB color.
        - random number for all parameters except the given parameter(s)
        - None argument(s) will be randomized, check with 'generator()'

        :param r: Red color value (0 to 1), defaults to None
        :param g: Green color value (0 to 1), defaults to None
        :param b: Blue color value (0 to 1), defaults to None
        :return: Tuple containing (R, G, B) color values
        """
        self.r = self.generator(r)
        self.g = self.generator(g)
        self.b = self.generator(b)
        return self.rgb

    def reset_color(self, r=None, g=None, b=None) -> tuple:
        """
        Reset RGB color values.
        - Reset only the given parameter(s) and don't change the others
        - None argument(s) won't be change

        :param r: New red color value (0 to 1), defaults to None
        :param g: New green color value (0 to 1), defaults to None
        :param b: New blue color value (0 to 1), defaults to None
        :return: Tuple containing (R, G, B) color values
        """
        self.r = r if r is not None else self.r
        self.g = g if g is not None else self.g
        self.b = b if b is not None else self.b
        return self.rgb
