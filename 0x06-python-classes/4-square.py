#!/usr/bin/python3
"""a module with a class handling getters and setters """


class Square:
    """a class handling getters and setters """
    def __init__(self, size=0):
        """runs upon instantiation"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """private size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculating the area"""
        return self.__size * self.__size
