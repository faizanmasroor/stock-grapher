from datetime import date

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf

today = date.today()


# Retrieves a Pandas DataFrame with the financial history of a stock
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


# Removes all finance-y columns other than the "High" column
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(columns=["Open", "Low", "Close", "Volume", "Dividends", "Stock Splits"], inplace=True)
    return df


# Filters the DataFrame passed as the argument such that it either includes only the last trading day (time_length =
# "Day") or the entire month which the last trading day belongs (time_length = "Month")
def filter_data(df: pd.DataFrame, time_length) -> pd.DataFrame:
    idx = -1
    while df.iloc[idx]['Day'] == today.day:
        idx -= 1
    df = df[df[time_length] == df.iloc[idx][time_length]]
    return df


# Changes the "DecimalHour" column so 9 hours and 30 minutes becomes 9.5 decimal hours (only used for the day DataFrame)
def hour_decimalize(df: pd.DataFrame) -> pd.DataFrame:
    df['DecimalHour'] = np.where(df['Minute'] == 30, df['Hour'] + 0.5, df['Hour'])
    return df


tk = yf.Ticker("TMUS")

month_hist = get_data(tk, "3mo", "1d")
day_hist = get_data(tk, "5d", "30m")

month_hist = clean_data(month_hist)
day_hist = clean_data(day_hist)

month_hist = filter_data(month_hist, time_length='Month')
day_hist = filter_data(day_hist, time_length='Day')

day_hist = hour_decimalize(day_hist)

yesterday = date(day_hist.iloc[0]['Year'], day_hist.iloc[0]['Month'], day_hist.iloc[0]['Day'])
month_plot = sns.lineplot(x=month_hist.Day, y=month_hist.High)
plt.title(f"{yesterday.strftime('%B %Y')} TMUS Stock Price")
plt.xlim(0, 32)
plt.ylabel('High (USD)')
plt.grid()
plt.show()

day_plot = sns.lineplot(x=day_hist.DecimalHour, y=day_hist.High)
plt.title(f"{yesterday.strftime('%B %d, %Y')}, TMUS Stock Price (Last Trading Day)")
plt.xlim(9, 16)
plt.xlabel('Hour')
plt.ylabel('High (USD)')
plt.grid()
plt.show()
