from ApiClientBase import ApiClientBase

class ArticleClient(ApiClientBase):
    def __init__(self, base_url):
        ApiClientBase.__init__(self, base_url)

    def search(self, query, page_no=1, page_size=10):
        params = {
            "query": query,
            "page": page_no,
            "page-size": page_size
        }
        return self.get("/article-api/v1/articles", params=params).json()

