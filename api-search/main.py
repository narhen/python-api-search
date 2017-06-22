#!/usr/bin/env python

import falcon
from Search import Search

app = falcon.API()
app.add_route("/", Search())
