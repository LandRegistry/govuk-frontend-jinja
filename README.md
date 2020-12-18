# GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/govuk-frontend-jinja.svg)](https://pypi.org/project/govuk-frontend-jinja/)
![govuk-frontend 3.10.2](https://img.shields.io/badge/govuk--frontend%20version-3.10.2-005EA5?logo=gov.uk&style=flat)
[![Test](https://github.com/LandRegistry/govuk-frontend-jinja/workflows/Test/badge.svg)](https://github.com/LandRegistry/govuk-frontend-jinja/actions)

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macro ports that are kept up-to-date and 100% compliant with the [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A [comprehensive test suite](https://github.com/surevine/govuk-frontend-diff) ensures compliance against the latest, and every subsequent, GOV.UK Frontend release.

- Package: [https://pypi.org/project/govuk-frontend-jinja/](https://pypi.org/project/govuk-frontend-jinja/)
- Example app: [https://github.com/matthew-shaw/govuk-frontend-jinja-example](https://github.com/matthew-shaw/govuk-frontend-jinja-example)
- Live demo: [https://govuk-frontend-jinja.herokuapp.com/](https://govuk-frontend-jinja.herokuapp.com/)

## How to use

After running `pip install govuk-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = ChoiceLoader([
    PackageLoader('app'),
    PrefixLoader({
        'govuk_frontend_jinja': PackageLoader('govuk_frontend_jinja')
    })
])
```

## Running the tests

The tests are run in a GitHub actions pipeline but if you want to run them locally you will need to install [govuk-frontend-diff](https://github.com/surevine/govuk-frontend-diff).

There is a test server at `tests/utils/app.py` which you will need to run using the following command:

```bash
(cd tests/utils && python -m flask run --port 3000)
```

You can then run the tests using `govuk-frontend-diff` as follows:

```bash
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v3.10.2
```

This is all wrapped up in `./test.sh` for simplified running (Requires Docker).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LandRegistry/govuk-frontend-jinja/tags).

## Contributors

- [Matt Shaw](https://github.com/matthew-shaw) (Primary maintainer)
- [Andy Mantell](https://github.com/andymantell) (Original author)
