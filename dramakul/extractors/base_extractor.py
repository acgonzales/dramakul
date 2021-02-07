from abc import ABC, abstractmethod

from dramakul.util import create_session


class Extractor(ABC):
    name = ""
    regexes = []
    QUALITIES = ["360p", "480p", "720p", "1080p"]

    def __init__(self, url: str, session=None, referer: str = None):
        self.url = url
        self.data = None

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
    def preferred_stream_url(self):
        if not self.data:
            self.extract_url()
        return self.data["sources"][self.preferred_quality]

    @property
    def preferred_quality(self):
        if not self.data:
            self.extract_url()
        return self.data["preferred_quality"]

    @property
    def qualities(self):
        if not self.data:
            self.extract_url()
        return list(self.data["sources"].keys())
