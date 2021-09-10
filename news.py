import requests
from bs4 import BeautifulSoup
from time import sleep
bbc = "https://www.bbc.com/burmese"


class News:
    def __init__(self):
        self.links = []
        self.bbc()

    def bbc(self):
        requests_session = requests.session()
        response = requests_session.get(bbc)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        # many
        links = soup.findAll("a",class_="bbc-1fxtbkn evnt13t0")
        for i in links[1:7]:
            self.links.append({"links": i.get("href"),"texts":i.text})
        sleep(1)







