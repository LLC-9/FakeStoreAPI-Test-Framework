import pytest
from utils.config_util import get_config

class BaseAPI:
    def __init__(self):
        self.base_url = get_config()
        self.proxies = {"http": None, "https": None}


