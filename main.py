from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    while True:
        while True:
            ticker = input("Enter a stock's ticker symbol: ")
            r = requests.get(f"https://finance.yahoo.com/quote/{ticker}/")
            if r.status_code == 200:
                break
            print("Invalid ticker symbol.\n")

        soup = BeautifulSoup(r.content, "html.parser")
        title_tag = soup.find("h1", {"class": "svelte-3a2v0c"})
        value_tag = soup.find("fin-streamer", {"class": "livePrice"})

        title = title_tag.text
        value = value_tag.attrs['data-value']

        print(f"{title}: {value}\n")
