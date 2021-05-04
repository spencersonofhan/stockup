import csv
import time
import datetime
import requests
import configparser
import pandas as pd
import json
import os
import sys
from binance.client import Client

def cmdCheck():
    if (sys.argv[1] == "-h"):
        print("------------------------HELP------------------------")
        print("FLAGS")
        print("\t-h: Help")
        print("\t-s: Look up stock prices")
        print("\t-c: Look up cryptocurrency prices")
        sys.exit(0)
    elif (sys.argv[1] == "-c"):
        return False
    elif (sys.argv[1] == "-s"):
        return True
    else:
        print("\nERR: Include a flag with stock_up.py command!\n")
        print("FLAGS")
        print("\t-h: Help")
        print("\t-s: Look up stock prices")
        print("\t-c: Look up cryptocurrency prices")
        sys.exit(1)

def getStockSymbols():
    CWD = os.getcwd()
    File_Name = "symbols.csv"
    Path = os.path.join(CWD, File_Name)
    df = pd.read_csv(Path)

    user_symbols = []
    for i in range(df.shape[0]):
        user_symbols.append(df.iloc[i,0])

    return user_symbols

def getCryptoSymbols():
    CWD = os.getcwd()
    File_Name = "cryptosymbols.csv"
    Path = os.path.join(CWD, File_Name)
    df = pd.read_csv(Path)

    user_symbols = []
    for i in range(df.shape[0]):
        user_symbols.append(df.iloc[i,0].upper() + "USDT")

    return user_symbols

def buildURL():
    return "https://paper-api.alpaca.markets/v2/orders"

def getHeaders(fStocks):
    config = configparser.ConfigParser()
    config.read('.config')

    headers = {}
    if fStocks:
        headers = {
                    "keyId" : config['API']['APCA-API-KEY-ID'],
                    "secretKey" : config['API']['APCA-API-SECRET-KEY']
                  }
    else:
        headers = {
                    "keyId" : config['API']['BNCE-API-KEY-ID'],
                    "secretKey" : config['API']['BNCE-API-SECRET-KEY']
                  }

    return headers

# def getCrypto(symbols):





def main():
    now = datetime.datetime.now()
    currentDate = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

    if len(sys.argv) != 2:
        sys.exit(1)

    Find_Stocks = cmdCheck()
    
    credentials = getHeaders(Find_Stocks)
    symbols = []

    if Find_Stocks:
        symbols = getStockSymbols()
        STOCKS_BASE_URL = "https://paper-api.alpaca.markets/v2/orders"
        # getStocks()
    else: 
        client = Client(credentials['keyId'], credentials['secretKey'])
        symbols = getCryptoSymbols()

        print("CURRENT DATE: " + str(datetime.datetime.fromtimestamp(time.time())))
        for i in range(len(symbols)):
            candle = client.get_klines(symbol=symbols[i], interval=Client.KLINE_INTERVAL_30MINUTE)
            offset = int(time.time() - (candle[0][6] // 1000))
            openTime = datetime.datetime.fromtimestamp((candle[0][0] // 1000) + offset)
            closeTime = datetime.datetime.fromtimestamp((candle[0][6] // 1000) + offset)
            
            print(symbols[i])
            print("Open " + str(openTime))
            print("Close: " + str(closeTime))


    # url = buildURL()
    # heads = getHeaders()
    #
    # tData = {
    #         "symbol": "GOOGL",
    #         "qty": 1,
    #         "side": "buy",
    #         "type": "market",
    #         "time_in_force": "day"
    #         }
    #
    #
    #
    #
    # GETReq = requests.post(url, headers=heads, json=tData)
    # print(GETReq.content)


main()
