from datetime import date, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf


# Gets a stock's historical data and adds columns for specific time measures;
# a Ticker object, period, and interval are passed as arguments; a Pandas DataFrame is returned
def get_data(ticker: yf.Ticker, period, interval) -> pd.DataFrame:
    hist = ticker.history(period=period, interval=interval)
    hist['Timestamp'] = hist.index
    hist['Minute'] = hist.Timestamp.dt.minute
    hist['Hour'] = hist.Timestamp.dt.hour
    hist['DecimalHour'] = hist.Timestamp.dt.hour  # This column is updated via hour_decimalize()
    hist['Day'] = hist.Timestamp.dt.day
    hist['Month'] = hist.Timestamp.dt.month
    hist['Year'] = hist.Timestamp.dt.year
    return hist


# Removes undesired price columns in the DataFrame
def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=["Open", "Low", "Close", "Volume", "Dividends", "Stock Splits"], inplace=True)
    return df


# Adds 0.5 to the Hour value in each row that has 30 as the Minutes value
def hour_decimalize(df: pd.DataFrame) -> pd.DataFrame:
    df['DecimalHour'] = np.where(df['Minute'] == 30, df['Hour'] + 0.5, df['Hour'])
    return df


# Creates a today date for today's month and identifies the last trading day
# TODO: Change yesterday calculation, because certain weekdays may be holidays (non-trading days)
today = date.today()
yesterday = today
while yesterday.weekday() > 4:
    yesterday -= timedelta(days=1)

tk = yf.Ticker("TMUS")

month_hist = get_data(tk, "3mo", "1d")
day_hist = get_data(tk, "5d", "30m")

month_hist = filter_data(month_hist)
day_hist = filter_data(day_hist)

# Adjust DataFrames to only display data from the current month or yesterday, respectively
month_hist = month_hist[month_hist['Month'] == today.month]
day_hist = day_hist[day_hist['Day'] == yesterday.day]

day_hist = hour_decimalize(day_hist)

"""Only used for debugging."""
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(day_hist)

# Creates the plots for the month's and last trading day's stock prices
month_plot = sns.lineplot(x=month_hist.Day, y=month_hist.High)
plt.title(f"{today.strftime('%B %Y')} TMUS Stock Price")
plt.xlim(0, 32)
plt.ylabel('High (USD)')
plt.grid()
plt.show()

day_plot = sns.lineplot(x=day_hist.DecimalHour, y=day_hist.High)
plt.title(f"{today.strftime('%B %d, %Y')}, TMUS Stock Price (Last Trading Day)")
plt.xlim(9, 16)
plt.xlabel('Hour')
plt.ylabel('High (USD)')
plt.grid()
plt.show()
