# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-jinja/compare/2.3.0...main)

## [2.3.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.3.0) - 22/07/2022

### Added

- [GOV.UK Frontend v4.2.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.2.0) support
- [Pagination component](https://design-system.service.gov.uk/components/pagination/)

Thanks to [SentientHousePlant](https://github.com/SentientHousePlant)

## [2.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.2.0) - 18/05/2022

### Added

- [GOV.UK Frontend v4.1.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.1.0) support

## [2.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.1.0) -10/05/2022

### Added

- [GOV.UK Frontend v4.0.1](https://github.com/alphagov/govuk-frontend/releases/tag/v4.0.1) support

## [2.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/2.0.0) -04/01/2022

### Added

- [GOV.UK Frontend v4.0.0](https://github.com/alphagov/govuk-frontend/releases/tag/v4.0.0) support

### Removed

- Python 3.6 support

## [1.5.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.5.1) -14/10/2021

### Fixed

- Resolve incompatible dependencies with Flask 2.0.0 and greater

## [1.5.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.5.0) -14/10/2021

### Added

- Support for [Jinja v3.0.2](https://jinja.palletsprojects.com/en/3.0.x/changes/) and above, now that [this loop scoping bug](https://github.com/pallets/jinja/issues/1427) has been fixed.
- The above also means support for [Flask v2.0.0](https://flask.palletsprojects.com/en/2.0.x/changes/) and above
- Support for [Python v3.10](https://www.python.org/downloads/release/python-3100/)
- Compatibility and "how to use" documentation in the [README](README.md)

### Changed

- Update to [GOV.UK Frontend v3.14.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.14.0)
- The package now requires Jinja versions `<3.0.0>=3.0.2`

## [1.4.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.4.0) - 29/06/2021

### Changed

- Update to [GOV.UK Frontend v3.13.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.13.0)

## [1.3.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.3.0) - 21/05/2021

### Changed

- Update to [GOV.UK Frontend v3.12.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.12.0)
- Pin Jinja2 requirement to less than v3.0.0 due to [this bug](https://github.com/pallets/jinja/issues/1427) at time of release
- Exclude tests directory from distribution package

## [1.2.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.2.1) - 05/03/2021

### Added

- Clarification that this is a [GOV.UK Design System Community Resource](https://design-system.service.gov.uk/community/resources-and-tools/), created and maintained by HM Land Registry
- Issue templates for [bug reports](.github/ISSUE_TEMPLATE/bug_report.md) and [feature requests](.github/ISSUE_TEMPLATE/feature_request.md)
- Dependabot config to help keep requirements up to date
- [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md)
- [Contribution guidelines](CONTRIBUTING.md)
- [Support information](README.md#support)

## [1.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.2.0) - 09/02/2021

### Added

- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) component

### Changed

- Update to [GOV.UK Frontend v3.11.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.11.0)
- Empty data URI in PNG version of the header logo

### Fixed

- Missing install dependency on Jinja2

## [1.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.1.0) - 18/12/2020

### Added

- [Notification banner](https://design-system.service.gov.uk/components/notification-banner/) component support
- Text input [prefix and suffix](https://design-system.service.gov.uk/components/text-input/#prefixes-and-suffixes) support
- Custom `inputmode` in the date input component

### Changed

- Update to [GOV.UK Frontend v3.10.2](https://github.com/alphagov/govuk-frontend/releases/tag/v3.10.2)
- Update to [`govuk-frontend-diff v.1.1.1](https://github.com/surevine/govuk-frontend-diff/releases/tag/v1.1.1)

## [1.0.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.0.0) - 20/08/2020

### Changed

- Update to [GOV.UK Frontend v3.8.1](https://github.com/alphagov/govuk-frontend/releases/tag/v3.8.1)
- Hint component can render block-level elements as valid HTML
- Correctly camel case SVG attributes in the header and footer
- Optional parameter added to the input, textarea and character-count components to enable or disable the spellcheck attribute
- Dockerised test suite for easier local running

## [0.2.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.1) - 25/06/2020

### Changed

- Test suite now abstracted out and using [govuk-frontend-diff](https://github.com/surevine/govuk-frontend-diff/). Allows nodejs to be wholly removed from this repository and benefit from shared improvements to the govuk-frontend-diff test suite.

## [0.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.0) - 18/06/2020

### Added

- Test suite to test Jinja against Nunjucks rendered outputs, using example inputs from [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend)
- Python linting with [Flake8](https://pypi.org/project/flake8/) and JS linting with [Prettier](https://prettier.io/)
- CI pipeline using [GitHub Actions](https://github.com/LandRegistry/govuk-frontend-jinja/actions)

### Changed

- Move templates to a subfolder to simplify `PackageLoader` setup in consuming apps
- Recommend consuming apps use `ChoiceLoader` to access templates without a namespace prefix

### Fixed

- Error thrown in page template when `bodyAttributes` is specified
- Incorrect use of `+` to concatenate non-strings
- Radios, checkboxes and summary-list components referencing a variable inside the scope of a loop and expecting it to exist outside that scope later
- Jinja variable scoping issues using namespaces
- Length of navigation items in footer component that might not exist

## [0.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.1.0) - 12/06/2020

### Added

- Jinja macros for all components in [GOV.UK Frontend release v3.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.7.0)
- Python packaging for publishing to PyPi
