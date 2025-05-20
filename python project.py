 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'40',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2829cc5d-3064-45c4-812e-44d83b2d6bc4',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

import pandas as pd 

df=pd.json_normalize(data['data'])
df['timestamp']=pd.to_datetime('now')
df

#api runner to easily run the loop that i made next and get all the time data in my data

def apirunner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
  'start':'1',
  'limit':'40',
  'convert':'USD'
    }
    headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2829cc5d-3064-45c4-812e-44d83b2d6bc4',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)


    df=pd.json_normalize(data['data'])
    df['timestamp']=pd.to_datetime('now')
    df=df.append(df)


import os 
from time import time
from time import sleep 

for i in range(330):
    apirunner()
    print('apirunner completed succesfully')
    sleep(60) #every 1min run the programm above 
exit()

df=pd.json_normalize(data['data'])
df