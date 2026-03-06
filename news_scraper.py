import requests
from bs4 import BeautifulSoup

def anime_news_network():

    url = "https://www.animenewsnetwork.com/news/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    news = []

    for h in soup.find_all("h3")[:5]:
        news.append(h.text.strip())

    return news


def crunchyroll_news():

    url = "https://www.crunchyroll.com/news"
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    news = []

    for h in soup.find_all("h2")[:5]:
        news.append(h.text.strip())

    return news


def mal_news():

    url = "https://myanimelist.net/news"
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    news = []

    for h in soup.find_all("p",class_="title")[:5]:
        news.append(h.text.strip())

    return news


def get_all_news():

    news = []

    try:
        news += anime_news_network()
    except:
        pass

    try:
        news += crunchyroll_news()
    except:
        pass

    try:
        news += mal_news()
    except:
        pass

    return news