##################################################
# Built in library/module/package of Python
# https://docs.python.org/3/library/csv.html
import csv
import calendar
import datetime
from datetime import date

##################################################
now = datetime.datetime.now()
current_date = date.today()
current_weekday = calendar.day_name[current_date.weekday()]
##################################################

# Set variables to empty lists
data = []
new_data = []

# Open dat file that contains your sample data, using "r" for read.
with open("/home/ubadmin/Documents/personal-assistant/master_list.csv", "r") as f:
    # load csv.DictReader, this will set your column names to a dictionary such
    # as {"Task": "Walk to the store and back"}
    reader = csv.DictReader(f, delimiter=",")

    # append each line to a list to read later
    for line in reader:
        data.append(line)

# Now we can loop through data
for line in data:
    line['Priority'] = (int(line['Important'])*10)+int(line['Urgent'])

    if line['Period'] == "DAILY":
        new_data.append(line)

    if line['Period'] == "WEEKLY" and line['Due Date'] == current_weekday:
        new_data.append(line)

    if line['Period'] == "MONTHLY" and line['Due Date'] == "xxxx-xx-"+str(now.day):
        new_data.append(line)

    if line['Period'] == "YEARLY" and line['Due Date'] == "xxxx-"+str(now.month)+"-"+str(now.day):
        new_data.append(line)

    if line['Due Date'] == str(now.year)+"-"+str(now.month)+"-"+str(now.day):
        new_data.append(line)

with open(str(now.year)+"-"+str(now.month)+"-"+str(now.day)+".csv", "a") as f:
    # we will now call DictReader, and assign field names, equal to our csv file.
    writer = csv.DictWriter(f, fieldnames=["Number", "Period", "Due Date", "Time", "Important", "Urgent", "Priority", "Task"])
    # Write the header column
    writer.writerow({'Number': 'Number', 'Period': 'Period', 'Due Date': 'Due Date', 'Time': 'Time', 'Important': 'Important', 'Urgent': 'Urgent', 'Priority': 'Priority', 'Task': 'Task'})

    # Write new_data into the file
    for x in range (0, 100):
        for line in new_data:
            if line['Priority'] == x:
                writer.writerow({'Number': line['Number'], 'Period': line['Period'], 'Due Date': line['Due Date'], 'Time': line['Time'], 'Important': line['Important'], 'Urgent': line['Urgent'], 'Priority': line['Priority'], 'Task': line['Task']})

