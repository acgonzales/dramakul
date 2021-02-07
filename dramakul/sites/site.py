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
