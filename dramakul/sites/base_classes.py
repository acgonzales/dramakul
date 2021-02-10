from abc import ABC, abstractmethod
from typing import List

from dramakul.extractors import Extractor
from dramakul.util import create_session


class SearchResult:
    def __init__(self, site, title: str, url: str, meta={}):
        self.site = site
        self.title = title
        self.url = url
        self.meta = meta

    def get_info(self):
        return self.site.get_info(self.url)

    def __str__(self):
        return self.title


class Drama:
    def __init__(self, site, title: str, url: str, meta={}):
        self.site = site
        self.title = title
        self.url = url
        self.meta = meta
        self.episodes = []

    def __getitem__(self, i):
        return self.episodes[i]

    def __str__(self):
        return self.title


class Episode:
    def __init__(self, site, url: str, drama: Drama = None, episode_number: str = None, meta={}):
        self.site = site
        self.drama = drama
        self.episode_number = episode_number
        self.url = url
        self.meta = meta
        self.extractors = []

    @property
    def stream_url(self):
        if not self.extractors:
            self.extract()

        for extractor in self.extractors:
            if extractor.data:
                return extractor.preferred_stream_url
        return None

    def extract(self) -> List[Extractor]:
        return self.site.extract_episode(self)

    def __str__(self):
        return f"{self.drama} - {self.episode_number}"


class Site(ABC):
    name = ""
    domain = ""
    meta = {}

    def __init__(self):
        self.session = create_session()

    @abstractmethod
    def search(self, query, **kwargs) -> List[SearchResult]:
        pass

    @abstractmethod
    def get_info(self, url, **kwargs) -> Drama:
        pass

    @abstractmethod
    def get_episode(self, url, **kwargs) -> Episode:
        pass

    @abstractmethod
    def extract_episode(self, episode, **kwargs) -> List[Extractor]:
        pass

    def __str__(self):
        return self.name
