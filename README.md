# GOV.UK Frontend Jinja Macros

[![PyPI version](https://badge.fury.io/py/govuk-frontend-jinja.svg)](https://pypi.org/project/govuk-frontend-jinja/)
![govuk-frontend 4.8.0](https://img.shields.io/badge/govuk--frontend%20version-4.8.0-005EA5?logo=gov.uk&style=flat)
[![Python package](https://github.com/LandRegistry/govuk-frontend-jinja/actions/workflows/python-package.yml/badge.svg)](https://github.com/LandRegistry/govuk-frontend-jinja/actions/workflows/python-package.yml)

**GOV.UK Frontend Jinja is a [community tool](https://design-system.service.gov.uk/community/resources-and-tools/) of the [GOV.UK Design System](https://design-system.service.gov.uk/). The Design System team is not responsible for it and cannot support you with using it. Contact the [maintainers](#contributors) directly if you need [help](#support) or you want to request a feature.**

This repository provides a complete set of [Jinja](https://jinja.palletsprojects.com/) macros that are kept up-to-date and 100% compliant with the original [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) Nunjucks macros. Porting is intentionally manual rather than automated to make updates simpler than maintaining an automated conversion routine. A [comprehensive test suite](https://github.com/surevine/govuk-frontend-diff) ensures compliance against the latest, and every subsequent, GOV.UK Frontend release.

If you are looking to build a fully featured Flask app that integrates with [GOV.UK Frontend Jinja](https://github.com/LandRegistry/govuk-frontend-jinja) and [GOV.UK Frontend WTForms](https://github.com/LandRegistry/govuk-frontend-wtf) please use the [GOV.UK Frontend Flask](https://github.com/LandRegistry/govuk-frontend-flask) template repository to [generate your app](https://github.com/LandRegistry/govuk-frontend-flask/generate).

## Compatibility

The following table shows the version of GOV.UK Frontend Jinja that you should use for your targeted version of GOV.UK Frontend:

| GOV.UK Frontend Jinja Version | Target GOV.UK Frontend Version |
| ----------------------------- | ------------------------------ |
| [2.8.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.8.0) | [4.8.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.8.0) |
| [2.7.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.7.0) | [4.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.7.0) |
| [2.6.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.6.0) | [4.6.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.6.0) |
| [2.5.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.5.0) | [4.5.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.5.0) |
| [2.4.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.4.0) | [4.4.1](https://github.com/alphagov/govuk-frontend/releases/tag/v4.4.1) |
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
./govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v4.8.0
```

This is all wrapped up in `./test.sh` for simplified running (Requires Docker).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/LandRegistry/govuk-frontend-jinja/tags).

## How to contribute

We welcome contribution from the community. If you want to contribute to this project, please review the [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

### Update methodology

How to update this package following a new release of GOV.UK Frontend:

1. On `govuk-frontend`, compare the last compatible tag and the latest tag, e.g. <https://github.com/alphagov/govuk-frontend/compare/v4.3.1...v4.4.0>
2. If there are any changes to templates in `package/govuk/components/<component>/template.njk` read the diff and apply the same changes to the Jinja equivalent templates in `govuk_frontend_jinja/templates/components/<component>/macro.html`
3. Take into account any idiosyncrasies between how Nunjucks and Jinja would interpret that template. E.g. `None` checking nested attributes, checking array items lengths or logic operators such as `is`, `not` and `in`.
4. Run the tests [as described above](#running-the-tests)
5. Resolve any failing tests by comparing the expected HTML output with the actual HTML reported by the test tool
6. Add a new row to the [compatibility table](#compatibility) above to show which version of GOV.UK Frontend the next release of this package will be targeting.
7. Once all tests are passing follow the [contribution guidelines](CONTRIBUTING.md) to raise a pull request.
8. After the pull request has been merged, [create a new release](https://github.com/LandRegistry/govuk-frontend-jinja/releases/new) and tag following SemVer conventions.
9. [GitHub Actions](https://github.com/LandRegistry/govuk-frontend-jinja/actions/workflows/python-publish.yml) will run on the new tag to build the package and publish it to PyPI. Verify that the package has been updated with the latest release tag by checking [the project page](https://pypi.org/project/govuk-frontend-jinja/)

## Contributors

- [Matt Shaw](https://github.com/matthew-shaw) (Primary maintainer)
- [Andy Mantell](https://github.com/andymantell) (Original author)

See the full list of [contributors on GitHub](https://github.com/LandRegistry/govuk-frontend-jinja/graphs/contributors)

## Support

This software is provided _"as-is"_ without warranty. Support is provided on a _"best endeavours"_ basis by the maintainers and open source community.

If you are a civil servant you can sign up to the [UK Government Digital Slack](https://ukgovernmentdigital.slack.com/signup) workspace to contact the maintainers listed [above](#contributors) and the community of people using this project in the [#govuk-design-system](https://ukgovernmentdigital.slack.com/archives/C6DMEH5R6) channel.

Otherwise, please see the [contribution guidelines](CONTRIBUTING.md) for how to raise a bug report or feature request.
