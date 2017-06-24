import requests
import logging

class ApiClientBase:
    def __init__(self, base_url):
        self.__base_url = base_url
        self.__logger = logging.getLogger(self.__class__.__name__)

    def __url(self, path):
        return "{}{}".format(self.__base_url, path)

    def get(self, path, params=None):
        self.__logger.info("GET {}".format(self.__url(path)))
        return requests.get(self.__url(path), params=params)

