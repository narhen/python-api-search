from ApiClientBase import ApiClientBase

class LearningpathClient(ApiClientBase):
    def __init__(self, base_url):
        ApiClientBase.__init__(self, base_url)

    def search(self, query, page_no=1, page_size=10):
        params = {
            "query": query,
            "page": page_no,
            "page_size": page_size
        }
        return self.get("/learningpath-api/v1/learningpaths", params=params).json()

