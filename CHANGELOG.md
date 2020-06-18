# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-jinja/compare/0.2.0...master)

## [0.2.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.2.0)

### Added

- Test suite to test Jinja against Nunjucks rendered outputs, using example inputs from [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend)
- Python linting with [Flake8](https://pypi.org/project/flake8/) and JS linting with [Prettier](https://prettier.io/)
- CI pipeline using [GitHub Actions](https://github.com/LandRegistry/govuk-frontend-jinja/actions)

### Changed

- Move templates to a subfolder to simplify `PackageLoader` setup in consuming apps

### Fixed

- Error thrown in page template when `bodyAttributes` is specified
- Incorrect use of `+` to concatenate non-strings
- Radios, checkboxes and summary-list components referencing a variable inside the scope of a loop and expecting it to exist outside that scope later
- Jinja variable scoping issues using namespaces
- Length of navigation items in footer component that might not exist

## [0.1.0](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/0.1.0)

### Added

- Jinja macros for all components in [GOV.UK Frontend release v3.7.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.7.0)
- Python packaging for publishing to PyPi
