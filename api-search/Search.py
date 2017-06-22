import falcon

class Search:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Hello world!\n"