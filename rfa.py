import requests
from bs4 import BeautifulSoup
import time
rfa = "https://www.rfa.org/burmese"
import time



class RFANews:
    def __init__(self):
        self.links = []
        self.rfa()

    def rfa(self):
        requests_session=requests.session()
        response = requests_session.get(rfa)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        links = soup.select(selector=".single_column_teaser h2 a")
        for i in links[:6]:
            self.links.append({"links": i.get("href"),"texts":i.text})
        time.sleep(1)


