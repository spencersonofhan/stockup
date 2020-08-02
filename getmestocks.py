import requests
import json
import os

# IEX Cloud sandbox variables
sandboxUrl = 'https://sandbox.iexapis.com/'
sandboxToken = os.environ['IEX_TOKEN']

x = requests.get(sandboxUrl + 'stable/stock/ibm/financials?token='
+ sandboxToken)

print(json.loads(x.text)['symbol'])
