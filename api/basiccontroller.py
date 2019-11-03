from random import randint

from flask_restful import Resource, request

from api.api_request_connector import APIRequestConnector
from html_scrapper.my_scrapper import MyHTMLParser
from my_enum.type_query import TypeQuery


class BasicController(Resource):
    """
    Basic Controller that handles the first exercise of the test
    """

    def __init__(self) -> None:
        super().__init__()
        self.api_request_connector = APIRequestConnector()
        self.my_html_parser = MyHTMLParser()
        self.keywords_param = "keywords"
        self.proxies = "proxies"
        self.type = "type"

    def get(self):
        """
        Delegates the GET functionality of the REST Controller. Gathers the data and set up everything
        :return: List of URL as a JSON
        """
        is_valid = self._validate_body(request)
        if not is_valid:
            return {"error_msg": "Body not present in the query or missing fields"}, 400
        json = request.get_json()
        keywords = json[self.keywords_param]
        type_query = json[self.type]
        if self.proxies in json.keys():
            list_proxies = json[self.proxies]
            random_proxy = list_proxies[randint(0, len(list_proxies) - 1)]
            response = self.api_request_connector.request(keywords, TypeQuery.get_type_from_str(type_query),
                                                          proxy=random_proxy)
        else:
            response = self.api_request_connector.request(keywords, TypeQuery.get_type_from_str(type_query))
        self.my_html_parser.feed(str(response.content))
        return [{"url": elem} for elem in self.my_html_parser.get_list_urls()]

    def _validate_body(self, a_request):
        try:
            json = a_request.get_json()
            return all([param in json.keys() for param in [self.keywords_param, self.type]])
        except Exception:
            return False
