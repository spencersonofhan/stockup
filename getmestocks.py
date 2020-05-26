# This will fetch multiple (or one bulk) jsons for stock data that is in an excel file
# ^ put this in a file to be read

from alpha_vantage.timeseries import TimeSeries
import csv
import time
import datetime

now = datetime.datetime.now()
currentDate = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
print(currentDate)

# Weird note, apiKey can be anything and it will still
# return desired results. bug is in alpha_vantage module

with open('C:/Users/chugs/programming/python/stockup/key.txt') as f:
    apiKey = f.readline().strip()
ts = TimeSeries('apiKey')
    
stocks = {}
first = True
with open('bought.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if first: # I have styled my csv with a header row
            first = False
            continue
        if row[0] == '':
            continue     
        stocks[row[0]] = (row[0], row[2])
        
alphaLimitCheck = 0
for i in stocks.keys():
    if alphaLimitCheck == 5:
        alphaLimitCheck = 0
        print("AlphaVantage limit reached, waiting for 60 seconds...")
        time.sleep(60)
        
    try:
        timeTable, meta = ts.get_daily(symbol=i)
        alphaLimitCheck += 1
    except ValueError:
        continue
    print(timeTable['2020-05-22'])