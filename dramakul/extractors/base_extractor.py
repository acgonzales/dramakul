from abc import ABC, abstractmethod

from dramakul.util import create_session


class Extractor(ABC):
    name = ""
    regexes = []

    def __init__(self, url: str, session=None, referer: str = None, eager: bool = False):
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

        if eager:
            self.extract_url()

    @abstractmethod
    def extract_url(self):
        pass

    @property
    def data(self):
        if not self._data:
            self.extract_url()

            if not self._data:
                return {}
        return self._data

    @property
    def preferred_stream_url(self):
        return self.data.get("sources", {}).get(self.preferred_quality)

    @property
    def preferred_quality(self):
        return self.data.get("preferred_quality")

    @property
    def qualities(self):
        return list(self.data.get("sources", {}).keys())

    def __str__(self):
        return str(self.preferred_stream_url)
