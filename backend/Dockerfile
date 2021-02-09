FROM python:3.9-buster

USER root

RUN apt-get install default-libmysqlclient-dev -y

COPY api /code/backend/api
COPY setup.py /code/backend/

WORKDIR /code/backend
RUN pip3 install -e .[dev]

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "python:api.wsgi", "api:app"]