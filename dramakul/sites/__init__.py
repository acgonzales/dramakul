from dramakul.sites.base_classes import Site, SearchResult, Drama, Episode
from dramakul.sites.dramacool9 import Dramacool9

SITES = [Dramacool9]


def get_site(url, *args, **kwargs):
    for site in SITES:
        if site.domain in url or site.name.lower() in url:
            return site()
