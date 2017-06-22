FROM pypy:2-slim

COPY requirements.txt .
COPY api-search ./api-search
RUN pip install -r requirements.txt

CMD ["gunicorn", "--chdir", "api-search", "-b", "0:1234", "main:app"]
