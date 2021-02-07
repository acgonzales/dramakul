import importlib.metadata

name = "Dramakul"
DISTRIBUTION_METADATA = importlib.metadata.metadata(name)
description = DISTRIBUTION_METADATA["description"]
__version__ = DISTRIBUTION_METADATA["version"]
