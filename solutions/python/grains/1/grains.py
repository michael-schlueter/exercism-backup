"""Calculate the number of grains on a chessboard

This module provides functions to determine the number of grains on a chessboard. The amount of grains on a single square is doubled each time. So there is one grain on the first square, two on the second, four on the third etc.
"""

def square(number):
    """Determine the number of grains on a single square.
    
    Parameters:
        number (number): Needs to be between 1 and 64 because a chessboard has 64 squares

    Returns:
        number: Number of grains on a given square
        
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Determine the total number of grains on a chessboard.
    
    Returns:
        number: Total of all grains on all 64 squares of a chessboard 
    """
    sum = 0
    for i in range(1, 65):
        sum += square(i)
    return sum
