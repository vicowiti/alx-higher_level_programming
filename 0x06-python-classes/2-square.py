#!/usr/bin/python3
""" Raising exceptions in classes """


class Square:
    """ A class that defines a square """
    def __init__(self, size=0):
        """ Runs upon instantiation """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
