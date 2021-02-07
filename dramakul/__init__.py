import importlib.metadata

name = "dramakul"
DISTRIBUTION_METADATA = importlib.metadata.metadata(name)
__version__ = DISTRIBUTION_METADATA["version"]
