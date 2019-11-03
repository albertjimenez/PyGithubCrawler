from random import randint

from flask import request

from api.basiccontroller import BasicController
from html_scrapper.my_scrapper import MyExtraHTMLParser


class ExtraController(BasicController):
    """
    Controller with extra capabilities to perform the second exercise of the test
    """
    def __init__(self) -> None:
        super().__init__()
        self.my_extra_html_parser = MyExtraHTMLParser()

    def get(self):
        """
       Delegates the GET functionality of the REST Controller. Gathers the data and set up everything
       :return: List of objects containing URL, owner, language stats with name and percentage use, as a JSON
       """
        url_list = super().get()
        json_extra = []
        for a_url in url_list:
            _url = a_url["url"]
            stats = self._get_stats(_url, request)
            owner = self._get_owner_from_url(_url)
            json_extra.append({"url": _url,
                               "extra":
                                   {"owner": owner, "language_stats": stats}})

        return json_extra

    def _get_stats(self, url, a_request) -> dict:
        json = a_request.get_json()
        if self.proxies in json.keys():
            list_proxies = json[self.proxies]
            random_proxy = list_proxies[randint(0, len(list_proxies) - 1)]
            response = self.api_request_connector.request_extra(url,
                                                                proxy=random_proxy)
        else:
            response = self.api_request_connector.request_extra(url)
        self.my_extra_html_parser.feed(str(response.content))
        return self.my_extra_html_parser.get_lang_stats()

    def _get_owner_from_url(self, url) -> str:
        return url.split("https://github.com/")[1].split("/")[0]
