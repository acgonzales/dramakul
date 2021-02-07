from dramakul.extractors import Extractor


class Cloud9(Extractor):
    name = "Cloud9"
    regexes = ["cloud9", "https://cloud9.to"]

    def __init__(self, url, *args, **kwargs):
        super().__init__(url, *args)

    def extract_url(self):
        url = self.url.replace('https://cloud9.to/embed/',
                               'https://api.cloud9.to/stream/')
        res = self.session.get(url)

        if res.status_code not in [200, 304]:
            return None

        data = res.json()["data"]

        sources = {}

        for source in data["sources"]:
            height = source["height"]

            if height == 480:
                quality = "480p"
            elif height == 720:
                quality = "720p"
            elif height == 1080:
                quality = "1080p"
            else:
                quality = "360p"

            sources[quality] = source["file"]

        return {
            "sources": sources,
            "preferred_quality": list(sources.keys())[0],
            "meta": {
                "file_name": data["name"]
            }
        }
