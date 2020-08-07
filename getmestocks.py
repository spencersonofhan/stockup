from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json
import os

# https://www.youtube.com/watch?v=DOHg16zcUCc
# Followed this tutorial ^^^
# NOT MY CODE!

START_DATE = '2009-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

STOCK = 'UCO'

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', START_DATE, END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)
        print(stock_data.head(10))

    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling_mean': stock_data.rolling(window=20).mean(),
        'long_rolling_mean': stock_data.rolling(window=200).mean()
    }

def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    plt.style.use('dark_background')

    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling_mean'], label='20 day rolling mean')
    plt.plot(stats['long_rolling_mean'], label='200 day rolling mean')


    plt.xlabel('Date')
    plt.ylabel('Adj Close Price')
    plt.legend()
    plt.title('Stock price over time')

    plt.show()

get_data(STOCK)
# # IEX Cloud sandbox variables
# sandboxUrl = 'https://sandbox.iexapis.com/'
# sandboxToken = os.environ['IEX_TOKEN']
#
# x = requests.get(sandboxUrl + 'stable/stock/ibm/financials?token='
# + sandboxToken)
#
# print(json.loads(x.text)['symbol'])
