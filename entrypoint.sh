#!/bin/sh
export FLASK_APP=./daikon/api.py
flask --debug run -h 0.0.0.0 -p 5858
