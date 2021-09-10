import requests
from bs4 import BeautifulSoup
r = "https://www.reuters.com/places/myanmar"
import time


class RNews:
    def __init__(self):
        self.links = []
        self.r()

    def r(self):
        requests_session = requests.session()
        response = requests_session.get(r)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".story-content a")
        for i in a:
            self.links.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

