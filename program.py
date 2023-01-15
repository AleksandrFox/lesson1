from datetime import date
def saturdays_between_two_dates(start, end):
    return sum(x.weekday() == 5 for x in [date.fromordinal(i) for i in range(min(start.toordinal(), end.toordinal()), max(start.toordinal(), end.toordinal()) + 1)])


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))