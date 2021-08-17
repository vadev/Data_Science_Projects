import yfinance as yf 
import streamlit as st 

st.write(""" 
# Simple Stock Price App 
# 
# Shown are the stock closing price and volume of Google
# """)

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get the data on this ticker symbol
tickerData = yf.Ticker(tickerSymbol) 

# Get the historical prices for this ticker symbol
tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2021-8-16")

st.line_chart(tickerDf.Close) 
st.line_chart(tickerDf.Volume)
