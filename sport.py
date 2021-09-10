import requests
from bs4 import BeautifulSoup
import time
eleven = "https://news-eleven.com/sports"
skysport = "https://www.skysports.com/"
skysportone = "https://www.skysports.com/football"
nytimes = "https://www.nytimes.com/section/sports"
si = "https://www.si.com/soccer"
euro = "https://www.eurosport.com/"
bbcsport = "https://www.bbc.com/sport"
fox = "https://www.foxnews.com/sports"



class Sport:
    def __init__(self):
        self.foxlinks = []
        self.skysportlinks = []
        self.nytimeslinks = []
        self.eurolinks = []
        self.silinks = []
        self.bbcsportlinks = []
        self.skysport()
        self.nytimes()
        self.si()
        self.euro()
        self.bbcsport()
        self.fox()




    def skysport(self):
        requests_session = requests.session()
        response = requests_session.get(skysport)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".sdc-site-tile__headline-link ")
        for i in a:
            self.skysportlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def nytimes(self):
        requests_session = requests.session()
        response = requests_session.get(nytimes)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".css-1l4spti a")
        for i in a:
            self.nytimeslinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def si(self):
        requests_session = requests.session()
        response = requests_session.get(si)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".m-ellipsis a")
        for i in a:
            self.silinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def euro(self):
        requests_session = requests.session()
        response = requests_session.get(euro)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".card-hover")
        for i in a:
            self.eurolinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def bbcsport(self):
        requests_session = requests.session()
        response = requests_session.get(bbcsport)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".gs-c-promo-heading")
        for i in a:
            self.bbcsportlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def fox(self):
        requests_session = requests.session()
        response = requests_session.get(fox)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".collection-spotlight-cards  .content .article .info .info-header .title a")
        for i in a:
            self.foxlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)











