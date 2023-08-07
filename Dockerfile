FROM python:3.8.6-slim-buster

WORKDIR /usr/src/daikon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN pip install Flask \
    Flask-SQLAlchemy \
    Flask-RESTful \
    flask-marshmallow \
    Flask-Caching \
    psycopg2-binary

COPY entrypoint.sh .
COPY daikon ./daikon

EXPOSE 5858

ENTRYPOINT ["/usr/src/daikon/entrypoint.sh"]
