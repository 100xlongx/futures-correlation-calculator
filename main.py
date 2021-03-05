# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:25:14 2021

@author: raaed
"""

import pandas_datareader.data as pdr
import numpy as np
import pandas as pd
import datetime
import time

import requests

ticker = "MSFT"

#GET /markets/{market_name}/candles?resolution={resolution}&limit={limit}&start_time={start_time}&end_time={end_time}

ts = int(time.time() * 1000)

_market1Name = 'BTC-PERP'
_market2Name = 'ETH-PERP'

_resolution = '300'
_limit = '500'
_start_time = ''
_end_time = ''

ENDPOINT = 'https://ftx.com/api'

r1 = requests.get(ENDPOINT + '/markets/{market_name}/candles?resolution={resolution}&limit={limit}'.format(market_name = _market1Name, resolution=_resolution, limit=_limit))
r2 = requests.get(ENDPOINT + '/markets/{market_name}/candles?resolution={resolution}&limit={limit}'.format(market_name = _market2Name, resolution=_resolution, limit=_limit))

print(r1.json()['result'])

df1 = pd.DataFrame(r1.json()['result'])
df2 = pd.DataFrame(r2.json()['result'])

print(df2)