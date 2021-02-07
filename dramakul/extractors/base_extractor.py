from abc import ABC, abstractmethod

from dramakul.util import create_session


class Extractor(ABC):
    name = ""
    regexes = []

    def __init__(self, url: str, session=None, referer: str = None):
        self.url = url
        self._data = {}

        if session:
            self.session = session
        else:
            self.session = create_session()

        if referer:
            self.referer = referer
        else:
            self.referer = self.session.headers.get("Referer", "")

    @abstractmethod
    def extract_url(self):
        pass
    
    @property
    def data(self):
        if not self._data:
            self.extract_url()
        return self._data

    @property
    def preferred_stream_url(self):
        if not self._data:
            self.extract_url()
        return self._data["sources"][self.preferred_quality]

    @property
    def preferred_quality(self):
        if not self._data:
            self.extract_url()
        return self._data["preferred_quality"]

    @property
    def qualities(self):
        if not self._data:
            self.extract_url()
        return list(self._data["sources"].keys())
