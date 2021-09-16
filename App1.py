# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:57:26 2021

@author: Leo Shi
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App 
Shown are the stock **closing price** and **volume** of Google!
""")

tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)
tickerDf  = tickerData.history(period = "id",start = '2010-5-31', end = '2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)