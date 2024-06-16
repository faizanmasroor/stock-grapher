import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests as rq
import seaborn as sns
import yfinance as yf

# String variables storing user input
ticker = ""
period = ""
interval = ""
save_req = ""
# List storing ticker symbols chosen by user
tickers = []
bools = ["y", "n"]

# Constant; includes all valid period and interval params. for yfinance functions
valid_periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
valid_intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]

if __name__ == "__main__":
    # Gathers ticker symbols from the user until they escape by typing "EXIT"
    print("""Type the ticker symbols of the stocks you wish to analyze.
Invalid ticker symbols will automatically be excluded in the analysis.
Once you are finished entering ticker symbols, type 'EXIT'.\n""")
    while True:
        ticker = input(">>> ").upper()
        if ticker == "EXIT":
            break
        tickers.append(ticker)

    # Similar approach as above; only accepts a valid period from the list
    print(f"""
Choose the period of analysis:
{valid_periods}\n""")
    while True:
        period = input(">>> ").lower()
        if period in valid_periods:
            break
        print("Invalid period entered.")

    print(f"""
Choose the interval of analysis:
{valid_intervals}\n""")
    while True:
        interval = input(">>> ").lower()
        if interval in valid_intervals:
            print("")
            break
        print("Invalid interval entered.")

    # Creates a Pandas DataFrame with historical data of all stocks (Series if just ones tock);
    # filters out invalid stocks
    df = yf.download(" ".join(tickers), period=period, interval=interval)
    df = df.dropna(axis=1, how="all")
    df = df['Adj Close']

    # Plots stock prices as a graph and saves png files per user request;
    # 1 stock -- if-clause, 2 or more stocks -- else-clause
    x = np.arange(len(df.index))
    if isinstance(df, pd.Series):
        y = df.values
        plt.plot(x, y)
        plt.title(tickers[0])
        plt.show(block=False)
        while (not save_req) or (save_req not in bools):
            save_req = input("Save graph in current directory? [y/n]: ").lower()
        if save_req == "y":
            plt.savefig(f"{tickers[0]}.png")
        plt.close()
        save_req = ""
    else:
        for name, values in df.items():
            y = values.to_numpy()
            plt.plot(x, y)
            plt.title(name)
            plt.show(block=False)
            while (not save_req) or (save_req not in bools):
                save_req = input("Save graph in current directory? [y/n]: ").lower()
            if save_req == "y":
                plt.savefig(f"{name}.png")
            plt.close()
            save_req = ""
