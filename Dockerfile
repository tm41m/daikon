FROM python:3.8.6-slim-buster

WORKDIR /usr/src/daikon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh .
COPY daikon ./daikon

EXPOSE 5858

ENTRYPOINT ["/usr/src/daikon/entrypoint.sh"]
