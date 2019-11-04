from api.api_request_connector import APIRequestConnector
from html_scrapper.my_scrapper import MyHTMLParser, MyExtraHTMLParser
from my_enum.type_query import TypeQuery

api_request = APIRequestConnector()
regular_parser = MyHTMLParser()
extra_parser = MyExtraHTMLParser()
URL = "https://github.com/albertjimenez/PyCppCompiler"
proxy = "https://193.41.88.58:53281"
keywords = ["openstack",
            "nova",
            "css"]

"""
This test covers 100% of the html_scrapper module and 93% of the api_request_connector.py
"""


def test_request_without_proxy():
    assert api_request is not None
    response = api_request.request(keywords=keywords, type_query=TypeQuery.REPO)
    assert response.status_code == 200
    regular_parser.feed(str(response.content))
    assert len(regular_parser.get_list_urls()) == 2


def test_request_extra_without_proxy():
    assert api_request is not None
    response = api_request.request_extra(url=URL)
    assert response.status_code == 200
    extra_parser.feed(str(response.content))
    assert len(extra_parser.get_lang_stats()) == 2
    assert "C++" in extra_parser.get_lang_stats() and "Python" in extra_parser.get_lang_stats()


"""
These tests below can only run once or twice in a while due to Github restrictions with proxies
"""
# def test_request_with_custom_proxy():
#     assert api_request is not None
#     response = api_request.request(keywords=keywords, type_query=TypeQuery.REPO, with_custom_proxy=True)
#     assert response.status_code == 200
#     regular_parser.feed(str(response.content))
#     assert len(regular_parser.get_list_urls()) == 2
#
# def test_request_with_request_proxy():
#     assert api_request is not None
#     response = api_request.request(keywords=keywords, type_query=TypeQuery.REPO, proxy=proxy)
#     assert response.status_code == 200
#     regular_parser.feed(str(response.content))
#     assert len(regular_parser.get_list_urls()) == 2
#
