#!/usr/bin/env bash
set -e

flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=120 --statistics
(cd tests/utils && nohup python -m flask run --port 3000 &)
wait-for-it localhost:3000
govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v5.13.0 --exclude page-template --ci
