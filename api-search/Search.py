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
        self.__register_client(article_cli, self.__parse_article_results)

        learningpath_cli = LearningpathClient(learningpath_api_url)
        self.__register_client(learningpath_cli, self.__parse_learningpath_results)

    def __register_client(self, client, parser_func):
        cli = Dict({
            "client": client,
            "parser": parser_func
        })
        self.__clients.append(cli)

    def __extract_fields_from_dict(self, dic, fields):
        entry = {}
        for field in fields:
            if dic.get(field, None):
                entry[field] = dic[field]
        return entry

    def __get_entry_by_lang(self, lst, lang):
        return next(iter(filter(lambda x: x.language == lang, lst)), None)

    def __extract_lang_fields_from_dict(self, dic, fields, language):
        result = {}
        for field in fields:
            entry = self.__get_entry_by_lang(dic.get(field, []), language)
            if entry:
                result[field] = entry[field]
        return result

    def __parse_results(self, results, language, language_fields_to_keep, other_fields_to_keep, result_type):
        result = []
        for res in results.results:
            entry = self.__extract_lang_fields_from_dict(res, language_fields_to_keep, language)
            entry.update(self.__extract_fields_from_dict(res, other_fields_to_keep))
            result.append(entry)

        return {
            "type": result_type,
            "results": result
        }

    def __parse_article_results(self, results, lang):
        return self.__parse_results(results, lang, ["title", "introduction"], ["id"], "articles")

    def __parse_learningpath_results(self, results, lang):
        return self.__parse_results(results, lang, ["title", "introduction"], ["id"], "learningpaths") 

    def __search(self, query, language, page_size, page_no):
        def cli_search(c):
            search_result = Dict(c.client.search(query, page_size=page_size, page_no=page_no))
            return c.parser(search_result, language)

        ex = futures.ThreadPoolExecutor(max_workers=len(self.__clients))
        return list(ex.map(cli_search, self.__clients))

    def on_get(self, req, response):
        query = req.get_param("query") or ""
        language = req.get_param("language") or "nb"
        page_size = req.get_param("page-size") or 5
        page_no = req.get_param("page") or 1

        self.__logger.info("GET / query={}, language={}, page-size={}, page={}".format(query,
            language, page_size, page_no))

        response.status = falcon.HTTP_200
        response.body = dumps(self.__search(query, language, page_size, page_no))
