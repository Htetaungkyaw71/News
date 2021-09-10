import requests
from bs4 import BeautifulSoup
import time
nytech  = "https://www.nytimes.com/section/technology"
rtech = "https://www.reuters.com/technology/"
crunch = "https://techcrunch.com/"
buzz = "https://www.buzzfeednews.com/section/tech"
hacker = "https://news.ycombinator.com/"
vice = "https://www.vox.com/recode"


class Tech:
    def __init__(self):
        self.nylinks = []
        self.rtechlinks = []
        self.buzzlinks = []
        self.vicelinks = []
        self.crunchlinks = []
        self.hackerlinks = []
        self.buzz()
        self.vice()
        self.crunch()
        self.nytech()
        self.rtech()
        self.hacker()


    def nytech(self):
        requests_session = requests.session()
        response = requests_session.get(nytech)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".css-qrzo5d a")
        for i in a:
            self.nylinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def crunch(self):
        requests_session = requests.session()
        response = requests_session.get(crunch)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".post-block__title__link ")
        for i in a:
            self.crunchlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def rtech(self):
        requests_session = requests.session()
        response = requests_session.get(rtech)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".story-card")
        for i in a:
            self.rtechlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)



    def hacker(self):
        requests_session = requests.session()
        response = requests_session.get(hacker)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".storylink ")
        for i in a:
            self.hackerlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)

    def buzz(self):
        requests_session = requests.session()
        response = requests_session.get(buzz)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".newsblock-story-card__link")
        for i in a:
            self.buzzlinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)


    def vice(self):
        requests_session = requests.session()
        response = requests_session.get(vice)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        a = soup.select(selector=".c-entry-box--compact__title a")
        for i in a:
            self.vicelinks.append({"link": i.get("href"), "text": i.text})
        time.sleep(1)
















