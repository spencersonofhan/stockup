# This will fetch multiple (or one bulk) jsons for stock data that is in an excel file
# alphavantage api key: 7EK27RTPSHABVBMP
# ^ put this in a file to be read

from alpha_vantage.timeseries import TimeSeries

with open('C:/Users/chugs/programming/python/stockup/key.txt') as f:
    apiKey = f.readline().strip()

# Weird note, apiKey can be anything and it will still
# return desired results. bug is in alpha_vantage module
# not in my code

ts = TimeSeries('apiKey')
uco, meta = ts.get_daily(symbol='XOM')
print(uco['2020-05-22'])