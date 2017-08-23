import falcon
import logging
from json import dumps
from addict import Dict
from concurrent import futures

from Clients import ArticleClient, LearningpathClient
from settings import article_api_url, learningpath_api_url

class Search:
    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__clients = []

        article_cli = ArticleClient(article_api_url)
        self.__register_client(article_cli, ["title", "introduction", "id"], "articles")

        learningpath_cli = LearningpathClient(learningpath_api_url)
        self.__register_client(learningpath_cli, ["title", "introduction", "id"], "learningpaths")

    def __register_client(self, client, fields_to_keep, api_name):
        cli = Dict({
            "client": client,
            "parser": self.get_result_parser_cb(fields_to_keep, api_name)
        })
        self.__clients.append(cli)

    def get_result_parser_cb(self, fields_to_keep, result_type):
        def parse_cb(results):
            return {
                "type": result_type,
                "results": [{ key: res[key] for res in results.results for key in fields_to_keep}]
            }
        return parse_cb

    def __search(self, query, language, page_size, page_no):
        def cli_search(c):
            search_result = Dict(c.client.search(query, page_size=page_size, page_no=page_no))
            return c.parser(search_result)

        ex = futures.ThreadPoolExecutor(max_workers=len(self.__clients))
        return list(ex.map(cli_search, self.__clients))

    def on_get(self, req, response):
        query = req.get_param("query") or ""
        language = req.get_param("language") or "nb"
        page_size = req.get_param("page-size") or 2
        page_no = req.get_param("page") or 1

        self.__logger.info("GET / query={}, language={}, page-size={}, page={}".format(query,
            language, page_size, page_no))

        response.status = falcon.HTTP_200
        response.body = dumps(self.__search(query, language, page_size, page_no))
