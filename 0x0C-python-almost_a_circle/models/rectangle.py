#!/usr/bin/python3
"""
    Defines the 'Rectangle' class that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Rectangle area"""
        return (self.height * self.width)

    def display(self):
        """Prints rectangle in stdout"""
        for x in range(self.y):
            print("")
        for x in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if (len(args) == 0):
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    @staticmethod
    def validator(attribute, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(attribute))
        if (attribute == "x" or attribute == "y"):
            if (value < 0):
                raise ValueError("{} must be >= 0".format(attribute))
        elif (value <= 0):
            raise ValueError("{} must be > 0".format(attribute))

    def to_dictionary(self):
        """Returns dictionary representation"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y})
