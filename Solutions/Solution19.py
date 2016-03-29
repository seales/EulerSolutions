def find_sunday(start_date, begin_weekday):
    
    # Finds the day of the week in which Sunday falls.
    # For example, if the 1st of the month is Tuesday, then
    # Sunday corresponds to the 6th
    
    # NOTE: this is very input specific, more checks would improve
    
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i in range(len(days)):
        if begin_weekday == days[i]:
            days_until_sunday = start_date[1]
            while days[i % 6] != "Sun":
                i += 1
                days_until_sunday += 1
            return days_until_sunday + 1
    raise Exception("Invalid input.\n")


def sunday_count(start_date, begin_weekday, end_date):
    SUNDAY = find_sunday(start_date, begin_weekday)
    month_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    leap_year = False # TODO - check if current year is leapyear
    while start_date[2] <= end_date[2]:  # TODO - improve checking

        if start_date[1] == SUNDAY:  # the first is Sunday
            count += 1

        start_date[1] += 7  # additional week
        if start_date[1] > month_count[start_date[0]-1]:  # 0-index offset
            start_date[1] -= month_count[start_date[0]-1]  # ""

            start_date[0] += 1
            if start_date[0] == 13:
                start_date[0] = 1  # December -> January
                start_date[2] += 1  # Increment year
                if not leap_year and is_leap_year(start_date[2]):
                    month_count[1] = 29
                elif leap_year:
                    leap_year = not leap_year
                    month_count[1] = 28

    return count


def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


assert is_leap_year(1900) is False
assert is_leap_year(1800) is False
assert is_leap_year(2000) is True

# NOTE: 1.1.1901 was a Tuesday

assert sunday_count([1, 1, 1901], "Tue", [12, 31, 2000]) == 171