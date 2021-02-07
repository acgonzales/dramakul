from abc import ABC, abstractmethod

from dramakul.util import create_session


class Extractor(ABC):
    name = ""
    regexes = []
    QUALITIES = ["360p", "480p", "720p", "1080p"]

    def __init__(self, url: str, session=None, referer: str = None):
        self.url = url

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
