from html.parser import HTMLParser
from json import loads


class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs=True, with_extras=False):
        super().__init__(convert_charrefs=convert_charrefs)
        self.read_data = False
        self.list_urls = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if "data-hydro-click" in attr and "model_name" in attr[1]:
                    git_url = loads(attr[1])["payload"]["result"]["url"]
                    self.list_urls.append(git_url)

    def get_list_urls(self):
        return self.list_urls
