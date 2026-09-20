def is_leap_year(year):
    """ This function checks if a year is a leap year or not. """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

leap_year = is_leap_year(1990)
print(leap_year)