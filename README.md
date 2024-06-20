# Historical Stock Price Graph Generator

#### A straightforward Python script that generates and downloads line graphs of the historical high prices of any stock per user request

## Installation

Use git to clone this repository on your machine.
```powershell
git clone https://github.com/faizanmasroor/stock-grapher.git
```
Run the file with Python
```powershell
python stock-grapher/stock_grapher.py
```

## Required Dependencies
* Python 3.11  
* matplotlib 3.8  
* NumPy 1.26  
* Pandas 2.2  
* Seaborn 0.13  
* yfinance 0.2.40

## Video Demo
https://github.com/faizanmasroor/stock-grapher/assets/107204129/e7e0c289-0b7e-4f42-b416-ec8bcce25256

## Goal
<b> Present graphs to visualize any stock's historical high price on two scales: </b>
1) The current month, with prices for every day
2) The last trading day, with prices for every 30 minutes

## Methodology

* Prompt the user to enter a stock ticker symbol
* Create a yfinance Ticker object with the user's stock
* Use the Ticker's history method to generate long-term and short-term Pandas DataFrames
  * Month DataFrame (long-term) → last 3 months with records for each day
  * Day DataFrame (short-term) → last 5 days with records for every 30 minutes
* Remove all price columns from both DataFrames, except for the stock's "High" price
* Generate additional date and time columns in DataFrames (Year, Month, Day, Hour, etc.)
* Filter the DataFrames only to include[^1]:
  * Month DataFrame → data belonging to the last trading day's month
  * Day DataFrame → data belonging to the last trading day
* Generate and calculate values for a new column in the Day DataFrame called "DecimalHour"[^2]
* Plot, display, and save Seaborn line graphs for both DataFrames
  * Month DataFrame → (X: Day, Y: High Price)
  * Day DataFrame → (X: DecimalHour, Y: High Price)

[^1]: This is accomplished by reverse indexing each DataFrame and decrementing the index while the row 'Day' at said index matches the current date. Then, conditional expressions are used to select a subset of the original data, thus removing all rows that do not match the month or day (depending on which DataFrame filter_data() is called on) of those that belong to the row arrived at from the previous operation (conditional reverse indexing is used to locate the last trading day)
[^2]: The values for 'DecimalHour' are 0.5 greater than the 'Hour' value in rows where the 'Minutes' value is 30, otherwise, it is equal to the 'Hour' value.
