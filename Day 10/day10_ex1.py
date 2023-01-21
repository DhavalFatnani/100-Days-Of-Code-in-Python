"""
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.
"""


def is_leap(_year):
    if _year % 4 == 0:
        if _year % 100 == 0:
            if _year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(_year,_month):
    """
    :param _year: any year
    :type _year: int
    :param _month: any month
    :type _month: int
    :return: the number of days in the month in @param _month
    :rtype: int
    """
    if _month > 12 or _month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(_year):
        month_days[1] = 29
    day = month_days[_month-1]
    return day


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







