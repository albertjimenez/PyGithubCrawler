from html.parser import HTMLParser
from json import loads


class MyHTMLParser(HTMLParser):
    """
    MyHTMLParser implementatio of the class HTMLParser. Does a webscrapping over a predefined url to retrieve the
    URL repositories'
    """
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.list_urls = []

    def handle_starttag(self, tag, attrs):
        """
        Handles the instant when an HTML tag is opened
        :param tag: We care about the `a`tag
        :param attrs: we care about the `data-hydro-click`
        :return: None
        """
        if tag == 'a':
            for attr in attrs:
                if "data-hydro-click" in attr and "model_name" in attr[1]:
                    git_url = loads(attr[1])["payload"]["result"]["url"]
                    self.list_urls.append(git_url)

    def get_list_urls(self):
        """
        Gets the list of urls
        :return:
        """
        return self.list_urls


class MyExtraHTMLParser(MyHTMLParser):
    """
    Extends the functionality of MyHTMLParser with the ability to parse inside a repository to obtain the language stats
    """
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.lang_stats = {}

    def handle_starttag(self, tag, attrs):
        """
        Handles the instant when an HTML tag is opened
        :param tag: We care about the `span`
        :param attrs: We care about the `aria-label`
        :return: None
        """
        if tag == 'span':
            for attr in attrs:
                if attr[0] == "aria-label" and attr[1] != "in this repository" and attr[1] != "in all of GitHub":
                    splitted_attr = attr[1].split()
                    if len(splitted_attr) == 2:
                        lang, percent = attr[1].split()
                        self.lang_stats[lang] = float(percent[:-1])

    def get_lang_stats(self):
        """
        Gets the dictionary of language_stats
        :return: dict
        """
        return self.lang_stats
