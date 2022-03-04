#!/usr/bin/env python3
##################################################
# Built in library/module/package of Python
# https://docs.python.org/3/library/csv.html
import calendar
import csv
import datetime
import math
from datetime import date

##################################################
now = datetime.datetime.now()
current_date = date.today()
current_weekday = calendar.day_name[current_date.weekday()]

def convert_day_to_int(day):
    # convert name of day string into integer
    # case insensitive but MUST be spelt correctly
    return getattr(calendar, day.upper())

def find_delta(future_day=calendar.FRIDAY):
    # return positive number of days until next "future_day"
    naive_delta =  future_day - date.today().weekday()
    return naive_delta % 7

##################################################
def open_master():
    data = []

    # Open dat file that contains your sample data, using "r" for read.
    with open("/home/ubadmin/Documents/personal-assistant/master_list.csv", "r") as f:
        # load csv.DictReader, this will set your column names to a dictionary such
        # as {"Task": "Walk to the store and back"}
        reader = csv.DictReader(f, delimiter=",")
        # append each line to a list to read later
        for line in reader:
            data.append(line)

    return data

##################################################

def todays_data(data):
    # Set variables to empty lists
    new_data = []
    global_stretch = 32

    # Now we can loop through data
    for line in data:
        print("...working...")

        if line['Number'] != "":
            if line['Period'] == "DAILY":
                my_delta = 1
            elif line['Period'] == "WEEKLY":
                day = convert_day_to_int(line["Due Date"])
                my_delta = find_delta(day)
                if my_delta == 7:
                    my_delta = 1
            elif line['Period'] == "MONTHLY":
                day = line['Due Date'].replace("Xxxx", str(now.year))
                day = day.split("-")
                once_date = datetime.date(int(day[0]), now.month, int(day[2]))
                my_delta = once_date - current_date
                my_delta = my_delta.days
                if my_delta < 0:
                    once_date = datetime.date(int(day[0]), now.month+1, int(day[2]))
                    my_delta = once_date - current_date
                    my_delta = my_delta.days
            elif line['Period'] == "YEARLY":
                day = line['Due Date'].replace("Xxxx", str(now.year))
                day = day.split("-")
                once_date = datetime.date(int(day[0]), int(day[1]), int(day[2]))
                my_delta = once_date - current_date
                my_delta = my_delta.days
                if my_delta < 0:
                    my_delta = my_delta + 365
            elif line['Period'] == "ONCE":
                day = line['Due Date'].split("-")
                once_date = datetime.date(int(day[0]), int(day[1]), int(day[2]))
                my_delta = once_date - current_date
                my_delta = my_delta.days
                if my_delta < 0:
                    my_delta = 1

            if my_delta < global_stretch and line['Dependency'] == "":
                if line['Stretch'] == "":
                    line['Priority'] = (int(line['Important'])*10)+int(line['Urgent'])
                    adjusted_priority = line['Priority'] - ((my_delta / int(line['Priority'])) * .7)
                    new_data.append(line)
                elif line['Stretch'] != "" and my_delta <= int(line['Stretch']):
                    line['Priority'] = (int(line['Important'])*10)+int(line['Urgent'])
                    adjusted_priority = line['Priority'] - ((my_delta / int(line['Priority'])) * .7)
                    new_data.append(line)

    return new_data

##################################################

def write_file(new_data, suffix):
    # Write a new file with today's date and modified priorities based on today's date.

    with open(str(now.year)+"-"+str(now.month)+"-"+str(now.day)+suffix, "a") as f:
        # we will now call DictReader, and assign field names, equal to our csv file.
        writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Important", "Urgent", "Priority", "Category", "Dependency", "Stretch", "Task"])
        # Write the header column
        writer.writerow({'Number': 'Number', 'Period': 'Period', 'Due Date': 'Due Date', 'Time': 'Time', 'Important': 'Important', 'Urgent': 'Urgent', 'Priority': 'Priority', 'Category': 'Category', 'Dependency': 'Dependency', 'Stretch': 'Stretch', 'Task': 'Task'})

        # Write new_data into the file
        for x in range (0, 100):
            for line in new_data:
                if line['Priority'] == x:
                    writer.writerow({'Number': line['Number'], 'Period': line['Period'], 'Due Date': line['Due Date'], 'Time': line['Time'], 'Important': line['Important'], 'Urgent': line['Urgent'], 'Priority': line['Priority'], 'Category': line['Category'], 'Dependency': line['Dependency'], 'Stretch': line['Stretch'], 'Task': line['Task']})

##################################################
##################################################
def main():
    data = open_master()
    new_data = todays_data(data)
    suffix = "-master.csv"
    daily_master = write_file(new_data, suffix)
    suffix = "-working.csv"
    daily_working = write_file(new_data, suffix)
    print("Done!")

if __name__ == '__main__':
    print("Called as an exe")
    main()


