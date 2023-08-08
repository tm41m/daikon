FROM python:3.8.6-slim-buster

WORKDIR /usr/src/daikon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN pip install Flask \
    Flask-SQLAlchemy \
    flask-marshmallow \
    marshmallow-sqlalchemy \
    Flask-Caching \
    Flask-Limiter \
    psycopg2-binary \
    gunicorn

COPY entrypoint.sh .
COPY daikon ./daikon
