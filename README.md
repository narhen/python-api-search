# python-api-search

An experimental search API for NDLA

## How to run

Run API server
```
$ pip install virtualenv
$ virtualenv apisrc
$ source apisrc/bin/activate
$ pip install -r requirements.txt
$ gunicorn --chdir api-search/ --reload -b :1234 main:app
```

In another terminal
```
$ curl 0:1234
```
