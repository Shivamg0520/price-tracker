import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36"
        }
        self.response = requests.get(self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("h1", id="title")
        if title is not None:
            return title.text
        else:
            return "Title not found"
    def product_price(self):
        price = self.soup.find("span", class_="a-price-whole").get_text(strip=True)
        return price
    
apple = PriceTracker(url="https://www.amazon.in/iPhone-16-Pro-Max-256/dp/B0DGHW2SRL/ref=sr_1_4?crid=Y14BLV1U9BIZ&dib=eyJ2IjoiMSJ9.5Li4-Gl-8nmHyKprPoeN0qG38mRsatMKeZwCfwZkYSQPMeDri3EjV1oXJ9krZvezXn69fVKVWGEe8eEKlk8myKpuUp1L9ljvMHHfMFcrJwqRXqMaJ_514QfsJKPfM_HBuYYtE2d2Eq2Cwo4xAqeH4o4LrA_q6Lmvc-WSc1KYHd_sBX7Lj-VtnKYjr-G90empNXF7ii-VjhshToB6JI3Zn0piPQdwpFc1_wPE3saZ4o8.2ekgsFgm7wyDedyP8TkmBcpXGNQxTS7fgs-40NsPsao&dib_tag=se&keywords=i%2Bphone16%2Bpro%2Bmax%2B256&qid=1753747789&sprefix=i%2Bpho%2Caps%2C407&sr=8-4&th=1")
print(apple.product_title())
print(apple.product_price())