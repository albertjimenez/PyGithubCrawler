import os
from random import randint

from requests import get as GET, Response

from my_enum.type_query import TypeQuery


class APIRequestConnector:
    """
    API Request Connector class that encapsulates the logic of performing a request
    """
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
        """
        Returns a response for the provided parameters
        :param keywords: List of str keywords
        :param type_query: TypeQuery for distinguish the different queries
        :param with_custom_proxy: boolean to turn on a custom proxy stored in the resources folder
        :param proxy: If is None, no proxy will be used
        :return: Response object
        """
        params = self._transform_string_url(keywords, type_query)
        if proxy != None:
            return GET(self._URL, params=params,
                       proxies={"https": "https://" + proxy})
        return GET(self._URL, params=params, proxies={"https": self.selected_proxy} if with_custom_proxy else None)

    def request_extra(self, url: str, with_custom_proxy=False, proxy: str = None) -> Response:
        """
        Same functionality as request methof but it gathers the data from a not predefined url
        :param url: target url
        :param with_custom_proxy: boolean to turn on a custom proxy stored in the resources folder
        :param proxy: If is None, no proxy will be used
        :return: Response object
        """
        if proxy != None:
            return GET(url,
                       proxies={"https": "https://" + proxy})
        return GET(url, proxies={"https": self.selected_proxy} if with_custom_proxy else None)
