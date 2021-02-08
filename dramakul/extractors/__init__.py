from dramakul.extractors.base_extractor import Extractor
from dramakul.extractors.cloud9 import Cloud9
from dramakul.extractors.xstreamcdn import XStreamCDN
from dramakul.extractors.watchasian import Watchasian

EXTRACTORS = [Cloud9, XStreamCDN, Watchasian]


def get_extractor(url, *args, **kwargs) -> Extractor:
    for extractor in EXTRACTORS:
        for regex in extractor.regexes:
            if regex in url:
                return extractor(url, *args, **kwargs)
