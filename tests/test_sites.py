import unittest
import random

from dramakul.sites import SITES

QUERY = "beauty"


class TestSite(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sites = [site() for site in SITES]

    def test_site_functions(self):
        for site in self.sites:
            results = site.search(QUERY)
            assert len(results) > 0, site.name

            result = random.choice(results)
            drama = result.get_info()

            assert drama, site.name
            assert len(drama.episodes) > 0, site.name
