from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, ConnectionError


def conn_to_website(url):
    site = requests.get(url, timeout=3)
    return site.text


def find_price(html, stock):
    # creates soup object which allows for parsing functions and finds the element that holds the stock value
    soup = BeautifulSoup(html, 'html.parser')
    # finds fin-streamer tag with specific a specific class
    fin = soup.findAll('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    print(f"One {stock} share is worth: {fin[0].string}\n")


if __name__ == "__main__":
    print("""Welcome to the stock price finder!\n""")

    # continuously prompts the user for stock requests and includes error handling for a connection cannot be made to
    # the website, timeout, or the requested stock does not exist
    while True:
        target_stock = input("Enter the stock's ticker symbol in all caps: ")
        stock_url = 'https://finance.yahoo.com/quote/' + target_stock

        try:
            page_content = conn_to_website(stock_url)
        except Timeout:
            print("A timeout error occurred.\n")
            continue
        except ConnectionError:
            print("There was an issue connecting to the website.\n")
            continue

        try:
            find_price(page_content, target_stock)
        except IndexError:
            print("The stock you entered does not exist.\n")
            continue
