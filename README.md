# GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/govuk-frontend-jinja.svg)](https://pypi.org/project/govuk-frontend-jinja/)
![govuk-frontend 3.7.0](https://img.shields.io/badge/govuk--frontend%20version-3.7.0-005EA5?logo=gov.uk&style=flat)
[![Test](https://github.com/LandRegistry/govuk-frontend-jinja/workflows/Test/badge.svg)](https://github.com/LandRegistry/govuk-frontend-jinja/actions)

This repository contains [Jinja](https://jinja.palletsprojects.com/) macro ports of the [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend). This is currently up to date with [release v3.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.7.0).

## How to use

[Here](https://github.com/matthew-shaw/govuk-frontend-jinja-example) is a simple example Flask app that demonstrates how to import and use the GOV.UK Jinja macros.

After running `pip install govuk-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

loader = ChoiceLoader([
    PackageLoader('app'),
    PrefixLoader({
        'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja')
    })
])
app.jinja_loader = loader

```

## Running the tests

The tests are run in a GitHub actions pipeline but if you want to run them locally you will need to install [govuk-frontend-diff](https://github.com/surevine/govuk-frontend-diff).

There is a test server at `tests/utils/app.py` which you will need to run using the following command:

```bash
(cd tests/utils && python -m flask run --port 3000)
```

You can then run the tests using `govuk-frontend-diff` as follows:

```bash
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v3.7.0
```

This is all wrapped up in `./test.sh` for simplified running.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LandRegistry/govuk-frontend-jinja/tags).

## Contributors

- [Matt Shaw](https://github.com/matthew-shaw) (Primary maintainer)
- [Andy Mantell](https://github.com/andymantell) (Original author)
