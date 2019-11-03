import os
from random import randint

from requests import get as GET, Response

from my_enum.type_query import TypeQuery


class APIRequestConnector:
    def __init__(self):
        self._URL = "https://github.com/search?"
        proxies = self._load_proxy()
        self.selected_proxy = proxies[randint(0, len(proxies) - 1)]

    def _transform_string_url(self, keywords: list, type_query: TypeQuery) -> dict:
        return {'q': " ".join(keywords), "type": type_query.value}

    def _load_proxy(self):
        resource_path = os.path.dirname(__file__)[:-3] + "resource/proxies.txt"
        with open(resource_path) as proxy_file:
            proxy_list = [p.strip() for p in proxy_file.readlines()]
        return proxy_list

    def request(self, keywords: list, type_query: TypeQuery, with_custom_proxy=False, proxy: str = None) -> Response:
        params = self._transform_string_url(keywords, type_query)
        if proxy != None:
            return GET(self._URL, params=params,
                       proxies={"https": "https://" + proxy})
        return GET(self._URL, params=params, proxies={"https": self.selected_proxy} if with_custom_proxy else None)
