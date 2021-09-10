import requests
from bs4 import BeautifulSoup
import time
eonline  = "https://www.eonline.com/news"
abc = "https://abcnews.go.com/Entertainment/"
sky = "https://news.sky.com/entertainment"
h = "https://hollywoodlife.com/"
us = "https://www.usmagazine.com/"
e = "https://edition.cnn.com/entertainment"



class Entertainment:
    def __init__(self):
        self.eonlinelinks = []
        self.abclinks = []
        self.skylinks = []
        self.skyimg = ""
        self.elinks= []
        self.hlinks = []
        self.uslinks = []
        self.eimg = ""
        self.eonline()
        self.abc()
        self.sky()
        self.h()
        self.us()
        self.e()

    def eonline(self):
        requests_session =  requests.session()
        response = requests_session.get(eonline)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".widget__title")
        for i in a:
            self.eonlinelinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def abc(self):
        requests_session = requests.session()
        response = requests_session.get(abc)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".ContentRoll__Headline h2 .AnchorLink")
        for i in a:
            self.abclinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def sky(self):
        requests_session = requests.session()
        response = requests_session.get(sky)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".sdc-site-tile__headline-link")
        for i in a:
            self.skylinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def h(self):
        requests_session = requests.session()
        response = requests_session.get(h)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".five-story__post-link")
        for i in a:
            self.hlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def us(self):
        requests_session = requests.session()
        response = requests_session.get(us)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".content-card-link")
        for i in a:
            self.uslinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def e(self):
        requests_session = requests.session()
        response = requests_session.get(e)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".cd__headline a")
        for i in a:
            self.elinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)








