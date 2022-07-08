from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, ConnectionError


def find_price(stock):
    try:
        url = 'https://finance.yahoo.com/quote/' + stock

        # finds website of stock and gets its html
        site = requests.get(url, timeout=3)
        html = site.text

        # creates soup object which allows for parsing functions and finds the element that holds the stock value
        soup = BeautifulSoup(html, 'html.parser')
        # finds fin-streamer tag with specific a specific class
        fin = soup.findAll('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        if not fin:
            print("The stock you entered does not exist.")
            quit()
        print(f"One {stock} share is worth: {fin[0].string}")
    except Timeout:
        print("A timeout error occurred.")
    except ConnectionError:
        print("There was an issue while reaching the website.")
    finally:
        quit()


if __name__ == "__main__":
    request = input("Enter the stock's ticker symbol in all caps: ")
    find_price(request)
