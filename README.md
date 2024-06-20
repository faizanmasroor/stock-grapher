# Historical Stock Price Graph Generator via Pandas, Seaborn, and yfinance

## A straightforward and concise Python script that, as per user input of any valid stock ticker symbol, creates, displays, and saves two PNG files representing the current month's and last trading day's high prices of said stock.

This project was an experience for me to gain expertise working with the Pandas library, due to its prominence in data science, machine learning, and deep learning. Likewise, Seaborn is an excellent tool for data visualization, featuring countless variants of graphs and statistical plots. The Python file in this repo accomplishes its task through the following steps:

* Prompt the user to enter a stock ticker symbol
* Create a yfinance Ticker object with the user's stock
* Use the Ticker's history method to generate long-term and short-term Pandas DataFrames
  * Month DataFrame (long-term) --> last 3 months with records for each day
  * Day DataFrame (short-term) --> last 5 days with records for every 30 minutes
* Remove all price columns from both DataFrames, except for the stock's "High" price
* Generate additional date and time columns in DataFrames (Year, Month, Day, Hour, etc.)
* Filter the DataFrames to only include:[^1]
  * a) Month DataFrame --> data belonging to the last trading day's month
  * b) Day DataFrame --> data belonging to the last trading day
* Generate and calculate values for a new column in the Day DataFrame called "DecimalHour"[^2]
* Plot, display, and save Seaborn line graphs for both DataFrames
  * Month DataFrame --> (X: Day, Y: High Price)
  * Day DataFrame --> (X: DecimalHour, Y: High Price)

https://github.com/faizanmasroor/stock-grapher/assets/107204129/13d03bb9-267d-470b-9c7b-7e6d5b211129

[^1]: This is accomplished by reverse indexing each DataFrame and decrementing the index until today's date and the date of the row no longer match. Then, conditional selection of the Pandas DataFrame is done to match with the month or day of the newly located last trading day.
[^2]: The values for DecimalHour are 0.5 greater than the Hour value in rows where the Minutes value is 30, otherwise, it is equal to the Hour value
