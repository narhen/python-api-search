from os import environ

env = environ.get("NDLA_ENVIRONMENT", "local")
article_api_url = environ.get("ARTICLE_API_URL", "http://article-api.ndla-local")
