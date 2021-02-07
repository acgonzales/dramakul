import unittest

from dramakul.sites import SITES

QUERY = "beauty"


class TestSite(unittest.TestCase):
    def test_search(_):
        for name, data in SITES.items():
            site = data["cls"]()
            results = site.search(QUERY)
            assert len(results) > 0, name
