from datetime import datetime
import csv

data = []

with open("data.csv", "r") as f:
    reader = csv.DictReader(f, delimiter = ",")

    for line in reader:
        data.append(line)

currDate = datetime.now().strftime("%Y-%m-%d")
currDay = datetime.now().strftime("%A")

with open(f"{currDate}.csv", "a") as f:
    writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Task"])
    for line in data:
        writer.writerow({'Number': line['Number'], 'Period': line['Period'], 'Due Date': line['Due Date'], 'Time': line['Time'], 'Task': line['Task']})
        f.write("\n")