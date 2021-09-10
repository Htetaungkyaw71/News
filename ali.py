import requests
from bs4 import BeautifulSoup
ali = "https://www.aljazeera.com/where/myanmar/"
import time



class ALINews:
    def __init__(self):
        self.links = []
        self.ali()

    def ali(self):
        requests_session = requests.session()
        response = requests_session.get(ali)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".gc__title a")
        for i in a:
            self.links.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)




