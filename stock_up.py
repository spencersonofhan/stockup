import csv
import time
import datetime
import requests
import configparser

def getUserSymbols():
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

    file.close()
    return stocks

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

    userSymbols = getUserSymbols()

    url = buildURL()
    heads = getHeaders()

    tData = {
            "symbol": "GOOGL",
            "qty": 1,
            "side": "buy",
            "type": "market",
            "time_in_force": "day"
            }




    GETReq = requests.post(url, headers=heads, json=tData)
    print(GETReq.content)


main()
