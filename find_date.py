import datetime
import calendar
from datetime import date

now = datetime.datetime.now()
current_numerical_year = now.year
current_numerical_month = now.month
current_numerical_day = now.day

current_date = date.today()
current_weekday = calendar.day_name[current_date.weekday()]

print("Today's date is", current_date)
print("Year is", current_numerical_year)
print("Month number is", current_numerical_month)
print("Day number is", current_numerical_day)
print("The day of the week is", current_weekday)

