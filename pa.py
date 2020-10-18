from datetime import date
import calendar
import csv
import datetime

data = []

with open("data.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=",")

    for line in reader:
        data.append(line)

now = datetime.datetime.now()
current_numerical_year = now.year
current_numerical_month = now.month
current_numerical_day = now.day

current_date = date.today()
current_weekday = calendar.day_name[current_date.weekday()]


with open(str(current_numerical_year)+"-"+str(current_numerical_month)+"-"+str(current_numerical_day)+".csv", "a") as f:
    writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Task"])
    for line in data:
        print(line)
        writer.writerow({'Number': line['Number'], 'Period': line['Period'], 'Due Date': line['Due Date'], 'Time': line['Time'], 'Task': line['Task']})
        f.write("\n")

