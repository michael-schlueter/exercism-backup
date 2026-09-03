"""Classify triangles by their side lengths.

This module provides functions to determine whether a set of three
side lengths forms a valid triangle, and if so, to classify it as
equilateral, isosceles, or scalene.
"""

def isTriangle(sides):
    """Determine whether the given side lengths form a valid triangle.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (a, b, c)

    Returns:
        bool: True if the sides form a valid triangle, False otherwise

    """
    a, b, c = sides

    return a > 0 and b > 0 and c> 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    """Determine whether a triangle with the given sides is equilateral.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (a, b, c)

    Returns:
        bool: True if all three sides are equal, False otherwise

    """
    if isTriangle(sides):
        a, b, c = sides
        return a == b and b == c

    return False


def isosceles(sides):
    """Determine whether a triangle with the given sides is isosceles.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (a, b, c)

    Returns:
        bool: True if at least two sides are equal, False otherwise

    """
    if isTriangle(sides):
        a, b, c = sides
        return a == b or a == c or b == c
    return False


def scalene(sides):
    """Determine whether a triangle with the given sides is scalene.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (a, b, c)

    Returns:
        bool: True if all three sides have different lengths, False otherwise

    """
    if isTriangle(sides):
        a, b, c = sides
        return a != b and b != c and a != c
    return False
