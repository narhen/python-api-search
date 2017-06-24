import falcon
import logging
from json import dumps

from Clients import ArticleClient
from settings import article_api_url

class Search:
    def __init__(self):
        self.__article_cli = ArticleClient(article_api_url)
        self.__logger = logging.getLogger(self.__class__.__name__)

    def on_get(self, req, response):
        query = req.get_param("query") or ""
        self.__logger.info("GET / query={}".format(query))
        res = self.__article_cli.search(query)

        response.status = falcon.HTTP_200
        response.body = dumps(res)
