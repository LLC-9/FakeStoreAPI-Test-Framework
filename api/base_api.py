class BaseAPI:
    def __init__(self):
        self.base_url = "https://fakestoreapi.com"
        self.proxies = {"http": None, "https": None}