# daikon
Our REST API framework built on Flask.

# Quickstart

To set up a local development environment, you will need `docker`.

1) Build your image with `docker build -t tm41m/daikon:0.1 .`

2) Run a container of the application with `docker run --name daikon-api -d -p 5858:5858 tm41m/daikon:0.1`