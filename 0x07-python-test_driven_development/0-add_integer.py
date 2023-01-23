#!/usr/bin/python3
"""Module which adds two integer or float numbers"""
def add_integer(a, b=98):
    """Function to add two integer or float number and return theres sum"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)
    return (a + b)
