from requests import get as GET, Response
from my_enum.type_query import TypeQuery
from random import randint
import os


class APIRequestConnector:
    def __init__(self):
        self._URL = "https://github.com/search?"
        proxies = self._load_proxy()
        self.selected_proxy = proxies[randint(0, len(proxies) - 1)]

    def _transform_string_url(self, keywords: list, type_query: TypeQuery) -> dict:
        return {'q': " ".join(keywords), "type": type_query.name}

    def _load_proxy(self):
        resource_path = os.path.dirname(__file__)[:-3] + "resource/proxies.txt"
        with open(resource_path) as proxy_file:
            proxy_list = [p.strip() for p in proxy_file.readlines()]
        return proxy_list

    def request(self, keywords: list, type_query: TypeQuery, with_proxy=False) -> Response:
        params = self._transform_string_url(keywords, type_query)
        return GET(self._URL, params=params, proxies={"https": self.selected_proxy} if with_proxy else None)

