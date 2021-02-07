import requests
from bs4 import BeautifulSoup

from dramakul.constants import get_random_headers


def create_session(headers=get_random_headers()):
    session = requests.Session()
    session.headers.update(headers)
    return session


def soupify(html):
    return BeautifulSoup(html, "html.parser")
