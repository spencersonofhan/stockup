import csv
import time
import datetime

now = datetime.datetime.now()
currentDate = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
print(currentDate)

stocks = []
header = True
with open('bought.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # CSV header
        if header:
            header = False
            continue
        if row[0] == '':
            continue
        stocks.append(row[0])

print(stocks)
