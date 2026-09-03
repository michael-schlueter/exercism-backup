"""Classify triangles by their side lengths.

This module provides functions to determine whether a set of three
side lengths forms a valid triangle, and if so, to classify it as
equilateral, isosceles, or scalene.
"""

def is_triangle(sides):
    """Determine whether the given side lengths form a valid triangle.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (side_a, side_b, side_c)

    Returns:
        bool: True if the sides form a valid triangle, False otherwise

    """
    side_a, side_b, side_c = sides

    return side_a > 0 and side_b > 0 and side_c > 0 and side_a + side_b >= side_c and side_b + side_c >= side_a and side_a + side_c >= side_b

def equilateral(sides):
    """Determine whether a triangle with the given sides is equilateral.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (a, b, c)

    Returns:
        bool: True if all three sides are equal, False otherwise

    """
    if is_triangle(sides):
        side_a, side_b, side_c = sides
        return side_a == side_b == side_c

    return False


def isosceles(sides):
    """Determine whether a triangle with the given sides is isosceles.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (side_a, side_b, side_c)

    Returns:
        bool: True if at least two sides are equal, False otherwise

    """
    if is_triangle(sides):
        side_a, side_b, side_c = sides
        return side_a == side_b or side_a == side_c or side_b == side_c
    return False


def scalene(sides):
    """Determine whether a triangle with the given sides is scalene.

    Parameters:
        sides (tuple/list of int or float): The three side lengths (side_a, side_b, side_c)

    Returns:
        bool: True if all three sides have different lengths, False otherwise

    """
    if is_triangle(sides):
        side_a, side_b, side_c = sides
        return side_a != side_b and side_b != side_c and side_a != side_c
    return False
