from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json
import os

BEGINNING = '2012-01-01'
ENDING = str(datetime.now().strftime('%Y-%m-%d'))

STOCKS = []
stockData = []

# Reads and returns stock symbols from stocks.txt
def get_symbols():
    temp_stocks = []
    stockFile = open('stocks.txt')
    for line in stockFile:
        temp_stocks.append(line.rstrip())

    return temp_stocks

# Returns a list of Pandas DataFrames that hold historical price data
def getStockData(symbols):
    tempStockData = []
    for ticker in symbols:
        try:
            rawData = data.DataReader(ticker, 'yahoo', BEGINNING, ENDING)
            adj_close = selectData(rawData, 'Adj Close')
            tempStockData.append(adj_close)
        except RemoteDataError:
            print('\'{t}\' data not found'.format(t=ticker))

    return tempStockData

# Returns a dictionary of useful statistics
def getStats(stockData):
    return {
        'last': np.mean(stockData.tail(1)),
        'short_mean': np.mean(stockData.tail(20)),
        'long_mean': np.mean(stockData.tail(200)),
        'short_rolling_mean': stockData.rolling(window=20).mean(),
        'long_rolling_mean': stockData.rolling(window=200).mean(),
        'rolling_std': stockData.rolling(20).std(),
        'mult_returns': stockData.pct_change()[1:]
    }

# Returns specified column and reindexes, also forward fills nan's
def selectData(stockData, col):
    weekdays = pd.date_range(start=BEGINNING, end=ENDING)
    selectedData = stockData[col].reindex(weekdays)
    return selectedData.fillna(method='ffill')


# Uses matplotlib to create a simple graph
def createGraph(symbols, stockData):
    plt.style.use('dark_background')
    plt.subplots(figsize=(12, 8))
    for ticker in range(len(stockData)):
        stats = getStats(stockData[ticker])
        plt.plot(stockData[ticker], label=symbols[ticker])
        # plt.plot(stats['short_rolling_mean'], label='20 day rolling mean')
        # plt.plot(stats['long_rolling_mean'], label='200 day rolling mean')

    plt.xlabel('Date')
    plt.ylabel('Adj Close Price')
    plt.legend()
    plt.title('Stock price over time')

    plt.show()

def print_data(symbols, dataList):
    if dataList:
        for stock in range(len(dataList)):
            print("\n$!-- Stock data for \'{:s}\' --!$".format(symbols[stock]))
            print(dataList[stock])
    else:
        print("No data was found!")

STOCKS = get_symbols()
stockData = getStockData(STOCKS)
print_data(STOCKS, stockData)
createGraph(STOCKS, stockData)
