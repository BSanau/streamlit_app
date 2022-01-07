### streamlit code (I) ###


import yfinance as yf
import streamlit as st
import pandas as pd


# Testing streamlit (I)
# yfinance: To download historical market data from Yahoo! finance.
# To run the code in the cmd:
# - First go to the folder containing this script (Documents/Python/streamlit)
# - streamlit run myapp.py


# Header of the web application
st.write("""
# Simple Strock Price App 

Shown are the stock closing price and volume of Google!

""")

# Define the ticker symbol
tickerSymbol = "GOOGL" #"AAPL"
# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDF = tickerData.history(period = "1d", start = "2010-5-31", end = "2020-5-31")
# The content of this tickerDF will be comprised by the following columns:
# Open | High | Low | Close | Volume | Dividends | Stock Splits

# Show in the web the Close and Volume columns
st.write("""## Closing price""")
st.line_chart(tickerDF.Close)
st.write("""## Volume price""")
st.line_chart(tickerDF.Volume)

# Show a table
st.write("""
| Column1   | Column 2   |
|:---------:|:----------:|
| a         | 1          |
| b         | 2          |
| c         | 3          |
""")

st.write("\n")
# Read ans print csv
df = pd.read_csv("INPUT/df_test.csv", sep = ";")
st.write(df)