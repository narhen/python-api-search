from os import environ

env = environ.get("NDLA_ENVIRONMENT", "local")
article_api_url = environ.get("ARTICLE_API_URL", "http://article-api.ndla-local")
learningpath_api_url = environ.get("LEARNINGPATH_API_URL", "http://learningpath-api.ndla-local")
