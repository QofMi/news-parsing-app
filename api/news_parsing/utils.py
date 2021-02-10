import logging
import requests
from bs4 import BeautifulSoup


URL = 'https://news.ycombinator.com/news'

NEWS = []


def _get_html(url: str) -> str:
    """
    Парсинг HTML.
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def get_news() -> None:
    """
    Получение загаловка ссылки поста.
    """
    find_news = _get_html(URL).find_all('td', class_='title')
    for news in find_news:
        try:
            news_title = news.find('a').get_text()
            news_url = news.find('a').get('href')
            NEWS.append(news_title + "**" + news_url)
        except:
            pass
