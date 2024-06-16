import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

# String variables storing user input
ticker = ""
period = ""
interval = ""

# Constant; includes all valid boolean responses; period and interval parameters for yfinance functions
bools = ["y", "n"]
valid_periods = {
    "1d": 9,
    "5d": 10,
    "1mo": 11,
    "3mo": 12,
    "6mo": 13,
    "1y": 14,
    "2y": 15,
    "5y": 16,
    "10y": 17,
    "ytd": 18,
    "max": 19
}
valid_intervals = {
    "1m": 1,
    "2m": 2,
    "5m": 3,
    "15m": 4,
    "30m": 5,
    "60m": 6,
    "90m": 7,
    "1h": 8,
    "1d": 9,
    "5d": 10,
    "1wk": 10.5,
    "1mo": 11,
    "3mo": 12,
}


def print_data(df: pd.Series):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)


def plot_data(df: pd.Series):
    # Plots stock prices as a graph and saves png files per user request;
    save_req = ""
    x = np.arange(len(df.index))
    y = df.values
    plt.plot(x, y)
    plt.title(ticker)
    plt.xlabel("Time")
    plt.show(block=False)
    while (not save_req) or (save_req not in bools):
        save_req = input("Save graph in current directory? [y/n]: ").lower()
    if save_req == "y":
        plt.savefig(f"{ticker}.png")
    plt.close()


if __name__ == "__main__":
    print("Type the ticker symbol of the stock you wish to analyze.\n")
    ticker = input(">>> ").upper()

    # Prompts user for the period of analysis; re-prompts in the case of invalid inputs
    print(f"\nChoose the period of analysis:\n{list(valid_periods.keys())}\n")
    while True:
        period = input(">>> ").lower()
        if period in valid_periods:
            break
        print("Invalid period entered.")

    # Same approach as above, but for the interval of analysis
    print(f"\nChoose the interval of analysis:\n{list(valid_intervals.keys())}\n")
    while True:
        interval = input(">>> ").lower()
        if interval in valid_intervals:
            if valid_intervals[interval] < valid_periods[period]:
                print("")
                break
            print("Please enter an interval less than the time period.")
            continue
        print("Invalid interval entered.")

    # Creates a Pandas DataFrame with historical data of all stocks (Series if just ones tock);
    # filters out invalid stocks
    ticker_obj = yf.Ticker(ticker)
    hist = ticker_obj.history(period=period, interval=interval)
    hist.reset_index(inplace=True)
    if hist.empty:
        print("Invalid ticker symbol.")
        quit()

    hist["Day of Week"] = hist["Date"].dt.dayofweek
    print(hist)
