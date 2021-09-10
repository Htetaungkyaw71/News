from flask import Flask,redirect,request,url_for,render_template,flash
import requests
from flask_bootstrap import Bootstrap
from bs4 import BeautifulSoup
from news import News
from rfa import RFANews
from voa import VOANews
from ali import ALINews
from g import GNews
from r import RNews
from sport import Sport
from tech import Tech
from entertainment import Entertainment
import datetime


now = datetime.datetime.now()
time = now.strftime("%d %B %Y")

app = Flask(__name__)






Bootstrap(app)

news = News()
rfa = RFANews()
voa = VOANews()
r = RNews()
g = GNews()
ali = ALINews()


@app.route("/")
def home():
    links = news.links
    rfalinks = rfa.links
    voalinks = voa.links
    glinks = g.links[:7]
    rlinks = r.links[:7]
    alilinks = ali.links[:7]

    # entertainment
    entertainment = Entertainment()
    eonlinelinks = entertainment.eonlinelinks[:7]
    abclinks = entertainment.abclinks[:7]
    skylinks = entertainment.skylinks[:7]
    elinks = entertainment.elinks[:7]
    uslinks = entertainment.uslinks[:7]
    hlinks = entertainment.hlinks[:7]
    elink = entertainment.elinks[0]

    # tech
    tech = Tech()
    nylinks = tech.nylinks
    crunchlinks = tech.crunchlinks[:7]
    hackerlinks = tech.hackerlinks[:7]
    rtechlinks = tech.rtechlinks[:7]
    vicelinks = tech.vicelinks[:7]
    buzzlinks = tech.buzzlinks[:7]

    #sport
    sport = Sport()
    skysportlinks = sport.skysportlinks[1:9]
    nytimeslinks = sport.nytimeslinks[:3]
    silinks = sport.silinks[:7]
    eurolinks = sport.eurolinks[1:7]
    bbcsportlinks = sport.bbcsportlinks[:7]
    foxlinks = sport.foxlinks
    return render_template("garden-index.html",
                           links=links,
                           rfalinks=rfalinks,
                           voalinks=voalinks,
                           alilinks=alilinks,
                           glinks = glinks,
                           rlinks = rlinks,
                           time=time,

                           eonlinelinks=eonlinelinks,
                           abclinks=abclinks,
                           skylinks=skylinks,
                           elinks=elinks,
                           uslinks=uslinks,
                           hlinks=hlinks,
                           elink=elink,


                           nylinks=nylinks,
                           hackerlinks=hackerlinks,
                           crunchlinks=crunchlinks,
                           rtechlinks=rtechlinks,
                           vicelinks=vicelinks,
                           buzzlinks=buzzlinks,

                           skysportlinks=skysportlinks,
                           nytimeslinks=nytimeslinks,
                           silinks=silinks,
                           eurolinks=eurolinks,
                           bbcsportlinks=bbcsportlinks,
                           foxlinks=foxlinks,

                           )

@app.route("/contact",)
def contact():
    return render_template('garden-contact.html')


@app.route("/about")
def about():
    return render_template('about.html')








if __name__ == "__main__":
    app.run(debug=True)

