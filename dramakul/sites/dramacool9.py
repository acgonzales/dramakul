from dramakul.sites import Site
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

        results = soup.select("#main > ul > li")
        search_results = []
        for result in results:
            details = result.select_one("div.post-details")

            poster = result.select_one("figure > a > img")["data-original"]

            title_h2 = details.find("h2")
            title = title_h2.text
            url = title_h2.find("a")["href"]

            search_results.append({
                "title": title,
                "url": url,
                "poster": poster
            })
        return search_results

    def get_info(self, url, **kwargs):
        pass
