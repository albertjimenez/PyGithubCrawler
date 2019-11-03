from html.parser import HTMLParser
from requests_html import HTMLSession
from my_enum.type_query import TypeQuery
from api.api_request_connector import APIRequestConnector


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)



# url = APIRequestConnector().request(["css", "openstack", "nova"], TypeQuery.REPO).url
# session = HTMLSession()
# r = session.get(url)
# print(r.html.absolute_links)