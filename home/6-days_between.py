def days_diff(date1, date2):
    import datetime

    return abs((datetime.datetime(*date1) - datetime.datetime(*date2)).days)
