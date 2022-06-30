# GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/govuk-frontend-jinja.svg)](https://pypi.org/project/govuk-frontend-jinja/)
![govuk-frontend 4.2.0](https://img.shields.io/badge/govuk--frontend%20version-4.2.0-005EA5?logo=gov.uk&style=flat)
[![Python package](https://github.com/LandRegistry/govuk-frontend-jinja/actions/workflows/python-package.yml/badge.svg)](https://github.com/LandRegistry/govuk-frontend-jinja/actions/workflows/python-package.yml)

**GOV.UK Frontend Jinja is a [community tool](https://design-system.service.gov.uk/community/resources-and-tools/) of the [GOV.UK Design System](https://design-system.service.gov.uk/). The Design System team is not responsible for it and cannot support you with using it. Contact the [maintainers](#contributors) directly if you need [help](#support) or you want to request a feature.**

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macros that are kept up-to-date and 100% compliant with the original [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A [comprehensive test suite](https://github.com/surevine/govuk-frontend-diff) ensures compliance against the latest, and every subsequent, GOV.UK Frontend release.

- Package: [https://pypi.org/project/govuk-frontend-jinja/](https://pypi.org/project/govuk-frontend-jinja/)
- Demo app: [https://github.com/LandRegistry/govuk-frontend-jinja-demo](https://github.com/LandRegistry/govuk-frontend-jinja-demo)
- Live demo: [https://govuk-frontend-jinja.herokuapp.com/](https://govuk-frontend-jinja.herokuapp.com/)

## Compatibility

The following table shows the version of GOV.UK Frontend Jinja that you should use for your targeted version of GOV.UK Frontend:

| GOV.UK Frontend Jinja Version | Target GOV.UK Frontend Version |
| ----------------------------- | ------------------------------ |
| [2.3.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.3.0) | [4.2.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.2.0) |
| [2.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.2.0) | [4.1.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.1.0) |
| [2.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.1.0) | [4.0.1](https://github.com/alphagov/govuk-frontend/releases/tag/v4.0.1) |
| [2.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.0.0) | [4.0.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.0.0) |
| [1.5.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.5.1) | [3.14.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.14.0) |
| [1.4.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.4.0) | [3.13.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.13.0) |
| [1.3.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.3.0) | [3.12.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.12.0) |
| [1.2.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.2.1) | [3.11.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.11.0) |
| [1.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.1.0) | [3.10.2](https://github.com/alphagov/govuk-frontend/releases/tag/v3.10.2) |
| [1.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.0.0) | [3.8.1](https://github.com/alphagov/govuk-frontend/releases/tag/v3.8.1) |
| [0.2.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.1) | [3.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.7.0) |

Any other versions of GOV.UK Frontend not shown above _may_ still be compatible, but have not been specifically tested and verified.

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

### Calling a Macro in your template

To use a component in your project templates you must import and call the component macro and pass the relevant options, for example:

```html
{%- from 'govuk_frontend_jinja/components/button/macro.html' import govukButton -%}

{{ govukButton({
  'text': "Save and continue"
}) }}
```

The options available to each component macro can be found in the original [GOV.UK Design System Components](https://design-system.service.gov.uk/components/) documentation. Since this project is a like-for-like port, the only difference between the Nunjucks examples and their Jinja equivalents is having to quote key names, e.g. `'text'` instead of `text`.

## Running the tests

The tests are run in a GitHub actions pipeline but if you want to run them locally you will need to install [govuk-frontend-diff](https://github.com/surevine/govuk-frontend-diff).

There is a test server at `tests/utils/app.py` which you will need to run using the following command:

```bash
(cd tests/utils && python -m flask run --port 3000)
```

You can then run the tests using `govuk-frontend-diff` as follows:

```bash
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v4.0.0
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
