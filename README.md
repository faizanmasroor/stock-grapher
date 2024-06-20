# Historical Stock Price Graph Generator via Pandas, Seaborn, and yfinance

## A straightforward and concise Python script that, as per user input of any valid stock ticker symbol, creates, displays, and saves two PNG files representing the current month's and last trading day's high prices of said stock.

This project was an experience for me to gain experience working with the Pandas library, due to its importance in the majority of Pythonic data science, machine learning, and deep learning. Likewise, Seaborn is an excellent tool for data visualization, featuring countless variants of graphs and statistical plots. The Python file in this repo accomplishes its task through the following steps:

* Prompt the user to enter a stock ticker symbol
* Instantiate a yfinance's Ticker object with the user's case-insensitive input as an argument
* Call the Ticker's history method twice, each generating one Pandas DataFrame
  * The month chart will span the last 3 months and include a row for each day
  * The day chart will span the last 5 days and include a row for each 30 minutes
* Remove all price columns in both DataFrames except for the stock's 'High' price
* Filter the data to only include: a) rows belonging to the current month, or b) rows belonging to the last trading day, by using today's date with the datetime library[^1]
  * a) Reverse index the month DataFrame until the 'Day' value no longer matches today's 'Day', conditionally filter the DataFrame such that all remaining rows' 'Month' value matches that of the row at the previously calculated index
  * b) Reverse index the  day  DataFrame until the 'Day' value no longer matches today's 'Day', conditionally filter the DataFrame such that all remaining rows'  'Day'  value matches that of the row at the previously calculated index
* Generate a new column in the day DataFrame called 'DecimalHour', which is equal to the 'Hour' column's value + 0.5 if the 'Minute' column's value is 30
  * e.g., 9 hours and 30 minutes would generate 9.5 decimal hours
* Plot, display, and save Seaborn line graphs for both DataFrames

[^1]: This cumbersome logic is used because DataFrames generated by yfinance.Ticker.history() only feature trading days, thus leaving out weekends and weekday holidays