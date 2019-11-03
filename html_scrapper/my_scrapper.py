from html.parser import HTMLParser
from requests_html import HTMLSession
from my_enum.type_query import TypeQuery
from api.api_request_connector import APIRequestConnector
from json import loads

class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs=True, with_extras= False):
        super().__init__(convert_charrefs=convert_charrefs)
        self.read_data = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if "data-hydro-click" in attr and "model_name" in attr[1]:
                    git_url = loads(attr[1])["payload"]["result"]["url"]
                    print(git_url)

url = APIRequestConnector().request(["kotlin"], TypeQuery.WIKIS)
parser = MyHTMLParser()
parser.feed(str(url.content))
