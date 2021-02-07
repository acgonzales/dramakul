from abc import ABC, abstractmethod

from dramakul.util import create_session


class Site(ABC):
    name = ""
    domain = ""
    meta = {}

    def __init__(self):
        self.session = create_session()

    @abstractmethod
    def search(self, query, **kwargs):
        pass

    @abstractmethod
    def get_info(self, url, **kwargs):
        pass


class SearchResult:
    def __init__(self, site: Site, title: str, url: str, meta={}):
        self.site = site
        self.title = title
        self.url = url
        self.meta = meta

    def get_info(self):
        return self.site.get_info(self.url)
