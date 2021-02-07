from dramakul.extractors.base_extractor import Extractor
from dramakul.extractors.cloud9 import Cloud9
from dramakul.extractors.xstreamcdn import XStreamCDN

EXTRACTORS = [Cloud9, XStreamCDN]


def get_extractor(url, *args, **kwargs):
    for extractor in EXTRACTORS:
        for regex in extractor.regexes:
            if regex in url:
                return extractor(url, *args, **kwargs)
