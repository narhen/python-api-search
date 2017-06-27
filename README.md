# python-api-search



## How to run

Run API server
```bash
$ pip install virtualenv
$ virtualenv apisrc
$ source apisrc/bin/activate
$ pip install -r requirements.txt
$ ARTICLE_API_URL=http://0:30002 gunicorn --chdir api-search/ --reload -b :1234 main:app
```

In another terminal
```bash
$ curl 0:1234
```

## Examples

`GET /?query=norge&page-size=2`
```json
[
  {
    "type": "articles",
    "results": [
      {
        "introduction": "Innovasjon Norge har ansvar for gjennomføringen...",
        "id": "14074",
        "title": "Innovasjon Norge"
      },
      {
        "introduction": "Trykk på lenkene under her for å lese om ...",
        "id": "15617",
        "title": "Filmutdanning i Norge"
      }
    ]
  },
  {
    "type": "learningpaths",
    "results": [
      {
        "introduction": "<p>Etter at du har fullført denne læringsstien, ...",
        "id": 56,
        "title": "Samfunnsforhold og statsutvikling, 700-1500"
      },
      {
        "introduction": "<p>Når du har gjennomført ...",
        "id": 2,
        "title": "Historia og fortellingene om Norge"
      }
    ]
  }
]

```
