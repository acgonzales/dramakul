from dramakul.extractors import get_extractor
from dramakul.sites import Site, SearchResult, Drama, Episode
from dramakul.util import soupify


class Dramacool9(Site):
    name = "Dramacool9"
    domain = "https://www.dramacool9.co"
    meta = {
        "name": name,
        "domain": domain
    }

    def search(self, query, **kwargs):
        page = kwargs.get("page", 1)

        search_url = f"{self.domain}/page/{page}?s={query}"
        res = self.session.get(search_url)
        soup = soupify(res.content)

        search_results = []
        for result in soup.select("#main > ul > li"):
            details = result.select_one("div.post-details")

            poster = result.select_one("figure > a > img")["data-original"]

            title_h2 = details.find("h2")
            title = title_h2.text
            url = title_h2.find("a")["href"]

            search_results.append(SearchResult(self, title, url, meta={
                "poster": poster
            }))
        return search_results

    def get_info(self, url, **kwargs):
        res = self.session.get(url)
        soup = soupify(res.content)

        title = soup.select_one(
            "#drama-details > div.drama-details.wrapper > header > h1").text
        poster = soup.select_one(
            "#drama-details > figure > a > img")["data-original"]

        drama = Drama(self, title, url, meta={
            "poster": poster
        })

        for episode in soup.select("#all-episodes > ul > li"):
            anchor = episode.select_one("h3 > a")
            title = anchor.text
            url = anchor["href"]
            episode_number = title.split(" ")[-1]
            drama.episodes.append(Episode(self, episode_number, url, drama=drama, meta={
                "title": title
            }))
        return drama

    def extract_episode(self, episode: Episode, **kwargs):
        res = self.session.get(episode.url)
        soup = soupify(res.content)

        for server in soup.select("#w-server > div.serverslist"):
            extractor = get_extractor(server.get("data-server"))
            if extractor:
                episode.extractors.append(extractor)
        return episode.extractors
