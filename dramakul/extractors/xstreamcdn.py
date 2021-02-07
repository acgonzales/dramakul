from dramakul.extractors import Extractor


class XStreamCDN(Extractor):
    name = "XStreamCDN"
    regexes = ["xstreamcdn", "fcdn.stream", "https://fcdn.stream"]

    def __init__(self, url, *args, **kwargs):
        super().__init__(url, *args)

    def extract_url(self):
        data = self.session.post(
            "https://www.xstreamcdn.com/api/source/" + self.url.split("/")[-1]).json()
        data = data["data"]

        sources = {}

        for source in data:
            sources[source["label"]] = source["file"]

        self._data = {
            "sources": sources,
            "preferred_quality": list(sources.keys())[-1]
        }

        return self.data
