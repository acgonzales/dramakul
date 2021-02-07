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

    def __str__(self):
        return self.title


class Drama:
    def __init__(self, site: Site, title: str, url: str, meta={}):
        self.site = site
        self.title = title
        self.url = url
        self.meta = meta
        self.episodes = []

    def __str__(self):
        return self.title


class Episode:
    def __init__(self, site: Site, drama: Drama, episode_number: str, url: str, meta={}):
        self.site = site
        self.drama = drama
        self.episode_number = episode_number
        self.url = url
        self.meta = meta

    def __str__(self):
        return f"{self.drama.title} - {self.episode_number}"
