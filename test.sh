#!/usr/bin/env bash

set -e

docker build -f ./tests/utils/Dockerfile -t govuk-frontend-jinja-test .
docker run -t govuk-frontend-jinja-test
