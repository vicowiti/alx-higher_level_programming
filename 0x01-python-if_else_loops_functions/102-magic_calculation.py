#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a > b:
        if c < b:
            return a * b - c
        else:
            return a + b
    else:
        return a + b
