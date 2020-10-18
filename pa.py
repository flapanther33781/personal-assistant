##################################################
# Built in library/module/package of Python
# https://docs.python.org/3/library/csv.html
import csv

# Set a variable = to an empty list
data = []

# Open dat file that contains your sample data, using "r" for read.
with open("/home/ubadmin/Documents/personal-assistant/data.csv", "r") as f:
    # load csv.DictReader, this will set your column names to a dictionary such
    # as {"Task": "Walk to the store and back"}
    # we are using the delimiter of comma.
    reader = csv.DictReader(f, delimiter=",")

    # using a for loop we append each line to our empty list to read later
    for line in reader:
        data.append(line)

# Now we can loop through data
for line in data:
    # dictionaries can be accessed with the variable name in the for loop. In
    # this case "line", followed by brackets and quoted header name.
    # line['Task'] will print your task in each row.
    # the below here prints your Number, followed by the Task.
    print(line['Number'],line['Task'])

##################################################
import datetime
import calendar
from datetime import date

now = datetime.datetime.now()
current_numerical_year = now.year
current_numerical_month = now.month
current_numerical_day = now.day

current_date = date.today()
current_weekday = calendar.day_name[current_date.weekday()]

##################################################
# we set 5 variables, this way when you split your data up by commas, it assigned 
# them correctly. we use split(",") to split on comma
#number, period, due_date, due_time, task = input("New Task (split data by commas\nNumber, Period, Due Date, Time, Task:\n").split(",")

##################################################
# this time lets use "a" for append, as this will create a new file, and/or
# append new data
#with open("data.csv", "a") as f:
#    # we will now call DictReader, and assign field names, equal to our csv file.
#    writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Task"])
#    # now we write our user input into the file using dictionary 
#    # combining our headers and our variable {"header" : variable}
#    writer.writerow({'Number': number, 'Period': period, 'Due Date': due_date, 'Time': due_time, 'Task': task})
#    # now cause I am drawing a blank we will call our file f, and write a new
#    # line after each row using "\n"
#    f.write("\n")

with open(str(current_numerical_year)+"-"+str(current_numerical_month)+"-"+str(current_numerical_day)+".csv", "a") as f:
    # we will now call DictReader, and assign field names, equal to our csv file.
    writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Task"])
    # now we write our user input into the file using dictionary 
    # combining our headers and our variable {"header" : variable}
    for line in data:
        print(line)
        writer.writerow({'Number': number, 'Period': period, 'Due Date': due_date, 'Time': due_time, 'Task': task})
        # now cause I am drawing a blank we will call our file f, and write a new
        # line after each row using "\n"
        f.write("\n")

