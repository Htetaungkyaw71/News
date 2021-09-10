import requests
from bs4 import BeautifulSoup
g = "https://www.theguardian.com/world/myanmar"
import time



class GNews:
    def __init__(self):
        self.links = []
        self.g()

    def g(self):
        requests_session = requests.session()
        response = requests_session.get(g)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.find_all("a",class_="u-faux-block-link__overlay js-headline-text")
        for i in a:
            self.links.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)




