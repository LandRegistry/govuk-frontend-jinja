#!/usr/bin/env bash

set -e

flake8 .
(cd tests/utils && nohup python -m flask run --port 3000 &)
wait-for-it localhost:3000
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v5.0.0 --exclude page-template --ci
