def leap_year(year):
    """
    Determine whether a given year is a leap year.

    A year is a leap year if it is divisible by 4, except for years divisible by 100, unless they are also divisble by 400.

    Parameters:
    year: int (The year to check)

    Returns:
    bool (True if 'year' is a leap year, False otherwise.)

    Examples:
    >>> leap_year(2020)
    True
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


        
