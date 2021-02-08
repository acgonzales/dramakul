from dramakul.extractors import Extractor


class Watchasian(Extractor):
    name = "Watchasian"
    regexes = ["watchasian", "watchasian.cc", "embed.watchasian"]

    def __init__(self, url, *args, **kwargs):
        super().__init__(url, referer="https://embed.watchasian.cc/", *args, **kwargs)
        self.session.headers.update({
            "x-requested-with": "XMLHttpRequest"
        })

    def extract_url(self):
        url = self.url.replace("streaming", "ajax")
        data = self.session.get(url)

        if data.text == "No thing!":
            return None

        data = data.json()

        # NOTE: Just a blind guess
        # We can still get the HLS link here, but I'll omit it for now
        quality_map = {
            "HD P": "1080p"
        }

        default_source = ""
        sources = {}

        for source in data["source"]:
            quality = quality_map.get(source["label"], "480p")
            sources[quality] = source["file"]

            if source["default"]:
                default_source = quality

        self._data = {
            "sources": sources,
            "preferred_quality": default_source
        }

        return self.data
