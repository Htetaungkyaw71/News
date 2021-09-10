import requests
from bs4 import BeautifulSoup
voa = "https://www.voanews.com/"


class VOANews:
    def __init__(self):
        self.links = []
        self.voa()

    def voa(self):
        requests_session = requests.session()
        response = requests_session.get(voa)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".top-story__title-link")
        for i in a:
            self.links.append({"link": i.get("href"), "text": i.text})





new = VOANews()

