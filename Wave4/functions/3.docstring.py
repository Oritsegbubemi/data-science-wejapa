def readable_timedelta(days):
    """
    This is a function that converts integer (dates) to weeks and days.
    INPUT:
    an integer that represents days
    OUTPUT:
    the number of weeks and days of contained in the integer
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
