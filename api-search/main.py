#!/usr/bin/env python

import falcon
import logging.config
from Search import Search

logging.config.fileConfig('config/logging.ini')

app = falcon.API()
app.add_route("/", Search())
