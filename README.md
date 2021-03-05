# GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/govuk-frontend-jinja.svg)](https://pypi.org/project/govuk-frontend-jinja/)
![govuk-frontend 3.11.0](https://img.shields.io/badge/govuk--frontend%20version-3.11.0-005EA5?logo=gov.uk&style=flat)
![Build](https://github.com/LandRegistry/govuk-frontend-jinja/workflows/Build/badge.svg)

**This is a [GOV.UK Design System Community Resource](https://design-system.service.gov.uk/community/resources-and-tools/), created and maintained by HM Land Registry**

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macro ports that are kept up-to-date and 100% compliant with the [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A [comprehensive test suite](https://github.com/surevine/govuk-frontend-diff) ensures compliance against the latest, and every subsequent, GOV.UK Frontend release.

- Package: [https://pypi.org/project/govuk-frontend-jinja/](https://pypi.org/project/govuk-frontend-jinja/)
- Demo app: [https://github.com/LandRegistry/govuk-frontend-jinja-demo](https://github.com/LandRegistry/govuk-frontend-jinja-demo)
- Live demo: [https://govuk-frontend-jinja.herokuapp.com/](https://govuk-frontend-jinja.herokuapp.com/)

## How to use

After running `pip install govuk-frontend-jinja`, ensure that you tell Jinja where to load the templates from using the `PackageLoader` as follows:

```python
from flask import Flask
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader

app = Flask(__name__)

app.jinja_loader = ChoiceLoader(
    [
        PackageLoader("app"),
        PrefixLoader({"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}),
    ]
)
```

## Running the tests

The tests are run in a GitHub actions pipeline but if you want to run them locally you will need to install [govuk-frontend-diff](https://github.com/surevine/govuk-frontend-diff).

There is a test server at `tests/utils/app.py` which you will need to run using the following command:

```bash
(cd tests/utils && python -m flask run --port 3000)
```

You can then run the tests using `govuk-frontend-diff` as follows:

```bash
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v3.11.0
```

This is all wrapped up in `./test.sh` for simplified running (Requires Docker).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LandRegistry/govuk-frontend-jinja/tags).

## How to contribute

We welcome contribution from the community. If you want to contribute to this project, please review the [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## Contributors

- [Matt Shaw](https://github.com/matthew-shaw) (Primary maintainer)
- [Andy Mantell](https://github.com/andymantell) (Original author)

## Support

This software is provided _"as-is"_ without warranty. Support is provided on a _"best endeavours"_ basis by the maintainers and open source community.

If you are a civil servant you can sign up to the [UK Government Digital Slack](https://ukgovernmentdigital.slack.com/signup) workspace to contact the maintainers listed [above](#contributors) and the community of people using this project in the [#govuk-design-system](https://ukgovernmentdigital.slack.com/archives/C6DMEH5R6) channel.

Otherwise, please see the [contribution guidelines](CONTRIBUTING.md) for how to raise a bug report or feature request.
