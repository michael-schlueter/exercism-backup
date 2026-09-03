def leap_year(year):
    """Determine whether a given year is a leap year.
 
    Parameters:
        year (int): The year to check
 
    Returns:
        bool: True if 'year' is a leap year, False otherwise
 
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


        
