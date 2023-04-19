#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:00:01 2023

@author: asif
"""

import pandas as pd
import yfinance as yf
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=730)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('BTC-USD',start=start_date,end=end_date,progress=False)
data["Date"] = data.index
print(data["Date"])


data = data[["Date", "Open", "High","Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())
print(data.info())
print(data.columns)
print(data.isnull().sum())
# Above ....collected the latest data of Bitcoin prices for the past 730 days and then I have prepared it for any data science task. 
#Now lets have a look at the shape of this dataset to see if we are working with 730 rows or not
print(data.shape)

#lets visualize the change in bitcoin prices till today by using a candlestick chart

import plotly.graph_objects as go
import plotly.io as pio
#for working plotly pip install -U kaleido
#for printing in browser default = 'browser'
pio.renderers.default='svg'


figure = go.Figure(data = [go.Candlestick ( x=data["Date"],open = data["Open"],high = data["High"],low = data["Low"],close = data["Close"])])
figure.update_layout(title="Bitcoin Price Analysis",xaxis_rangeslider_visible=False)
figure.show()

#lets have a look at the correlation of all the columns in the data concerning the Close columns
correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))

#Predicting the future prices of cryptocurrency is based on the problem of Time Series analysis.
#The AutoTS library in python is one of the best libraries for time series analysis.
#using the AutoTS library to predict the bitcoin prices for the next 30 days
'''
from autots import AutoTS

model = AutoTS(forecast_length=30, frequency='infer', ensemble='simple') 
model = model.fit(data, date_col='Date', value_col = 'Close', id_col=None)
prediction = model.predict()
forecast = prediction.forecast
print(forecast)
'''