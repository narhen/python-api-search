import falcon
from json import dumps

from Clients import ArticleClient
from settings import article_api_url

class Search:
    def __init__(self):
        self.__article_cli = ArticleClient(article_api_url)

    def on_get(self, req, response):
        query = req.get_param("query") or ""
        res = self.__article_cli.search(query)

        response.status = falcon.HTTP_200
        response.body = dumps(res)
