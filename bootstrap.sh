#!/bin/sh
export FLASK_APP=./daikon/index.py
pipenv run flask --debug run -h 0.0.0.0
