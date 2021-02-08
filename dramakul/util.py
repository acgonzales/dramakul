from bs4 import BeautifulSoup
import jsbeautifier
import requests

from dramakul.constants import get_random_headers


def create_session(headers=get_random_headers()):
    session = requests.Session()
    session.headers.update(headers)
    return session


def soupify(html):
    return BeautifulSoup(html, "html.parser")


def beautify_js(js):
    return jsbeautifier.beautify(js)
