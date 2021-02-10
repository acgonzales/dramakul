from bs4 import BeautifulSoup
import jsbeautifier
import requests
from requests.adapters import HTTPAdapter

from dramakul.constants import get_random_headers


def create_session(headers=get_random_headers(), max_retries=5):
    adapter = HTTPAdapter(max_retries=max_retries)

    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update(headers)
    return session


def soupify(html):
    return BeautifulSoup(html, "html.parser")


def beautify_js(js):
    return jsbeautifier.beautify(js)
