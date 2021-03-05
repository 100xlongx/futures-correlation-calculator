# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:25:14 2021

@author: raaed
"""

#evolve this to show correlations for all pairs

import pandas_datareader.data as pdr
import numpy as np
import pandas as pd
import datetime
import time

import operator
import requests


#GET /markets/{market_name}/candles?resolution={resolution}&limit={limit}&start_time={start_time}&end_time={end_time}

def getCandles(df: pd.DataFrame, _marketName: str, _resolution = '300', _limit = '500'):
    r1 = requests.get(ENDPOINT + '/markets/{market_name}/candles?resolution={resolution}&limit={limit}'.format(market_name = _marketName, resolution=_resolution, limit=_limit))
    df1 = pd.DataFrame(r1.json()['result'])
    
    df[_marketName] = df1['close'];
    
    print('loading data from {name}'.format(name = _marketName))
    print(df)
    

ENDPOINT = 'https://ftx.com/api'

#Get the markets from the API
markets = requests.get(ENDPOINT + "/markets");

#parse the json results
result = markets.json()['result']

#create a list of all the names of futures markets
watchlist = list(map(operator.itemgetter('name'), filter(lambda d: d['type'] == 'future', result)))

#filter for perpetuals
watchlist = list(filter(lambda d: d.find('PERP') > 0, watchlist))

#print(list(filter(lambda d: d.find('PERP'), watchlist)))

df = pd.DataFrame()

#populate dataframe with marketcloses from markets
for ticker in watchlist:
    getCandles(df, ticker)

print(df.corr())
