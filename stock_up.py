import csv
import time
import datetime
import requests
import configparser
import pandas as pd
import json
import os
import sys

def getUserSymbols():
    CWD = os.getcwd()
    File_Name = "symbols.csv"
    Path = os.path.join(CWD, File_Name)
    df = pd.read_csv(Path)

    user_symbols = []
    for i in range(df.shape[0]):
        user_symbols.append(df.iloc[i,0])

    return user_symbols

def buildURL():
    return "https://paper-api.alpaca.markets/v2/orders"

def getHeaders():
    config = configparser.ConfigParser()
    config.read('.config')

    headers={
            "APCA-API-KEY-ID" : config['API']['APCA-API-KEY-ID'],
            "APCA-API-SECRET-KEY" : config['API']['APCA-API-SECRET-KEY']
            }

    return headers



def main():
    now = datetime.datetime.now()
    currentDate = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

    if len(sys.argv) != 2:
        sys.exit(1)

    Find_Stocks = True
    if (sys.argv[1] == "-h"):
        print("------------------------HELP------------------------")
        print("FLAGS")
        print("\t-h: Help")
        print("\t-s: Look up stock prices")
        print("\t-c: Look up cryptocurrency prices")
        sys.exit(0)
    elif (sys.argv[1] == "-c"):
        Find_Stocks = False
    elif (sys.argv[1] == "-s"):
        pass
    else:
        print("\nERR: Include a flag with stock_up.py command!\n")
        print("FLAGS")
        print("\t-h: Help")
        print("\t-s: Look up stock prices")
        print("\t-c: Look up cryptocurrency prices")
        sys.exit(1)
    
    symbols = getUserSymbols()
    if Find_Stocks:
        print(symbols[1])

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
