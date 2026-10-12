# Contributing

Thank you for your interest in contributing to GOV.UK Frontend Jinja. This guide explains how to report issues, set up a development environment, make and test changes, and propose them for review.

Please also follow the project's [code of conduct](CODE_OF_CONDUCT.md).

## Report an issue or suggest a feature

Before opening an issue, check the [existing issues](https://github.com/LandRegistry/govuk-frontend-jinja/issues). If someone has already reported the problem or suggested the feature, add any useful details to that discussion.

If there is no existing issue, [create a bug report or feature request](https://github.com/LandRegistry/govuk-frontend-jinja/issues/new/choose) using the appropriate template. Include the steps to reproduce a bug, what you expected to happen, and any relevant environment details. For feature requests, explain the problem the change would solve and any alternatives you have considered.

## Set up your development environment

The project uses [uv](https://docs.astral.sh/uv/) to manage Python versions, dependencies, and package builds. Install uv using its [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

The supported Python versions are 3.11 through 3.14. The `.python-version` file selects Python 3.14 as the default for local development; uv can install and use it when needed.

From the repository root, install the project and development dependencies:

```bash
uv sync --locked --all-groups
```

Run project commands through `uv run`, so they use the project's environment. For example:

```bash
uv run flake8 .
```

Add or remove dependencies with `uv add` or `uv remove` rather than editing `uv.lock` by hand. Add development-only dependencies to the `dev` group, for example `uv add --group dev <package>`.

## Make changes

GOV.UK Frontend Jinja is a manual, like-for-like port of GOV.UK Frontend's Nunjucks macros to Jinja templates. When changing a component:

1. Refer to the relevant [GOV.UK Design System component documentation](https://design-system.service.gov.uk/components/) and the corresponding upstream GOV.UK Frontend template.
2. Keep the Jinja macro behavior and rendered HTML aligned with the upstream component. Account for differences in how Jinja and Nunjucks handle expressions, such as `None`, nested attributes, collection lengths, and operators.
3. Keep changes focused, and check existing issues and [pull requests](https://github.com/LandRegistry/govuk-frontend-jinja/pulls) to avoid duplicating work.

When updating the package for a new GOV.UK Frontend release:

1. Compare the latest upstream release with the last version supported by this package. For example, use the upstream [release comparison](https://github.com/alphagov/govuk-frontend/compare/v6.3.0...v6.5.1).
2. Review changes to component templates under `package/govuk/components/<component>/template.njk` and apply relevant changes to the corresponding files in `govuk_frontend_jinja/templates/components/`.
3. Run the compatibility tests described below and resolve differences between expected and actual HTML.
4. Update the compatibility information in the [README](README.md) to identify the GOV.UK Frontend version being targeted.

## Run checks and tests

### Lint

Run the blocking lint check used in CI:

```bash
uv run --locked flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

CI also runs a non-blocking flake8 report for complexity and style information. The automated checks, including the Python-version matrix, are defined in [`.github/workflows/python-package.yml`](.github/workflows/python-package.yml).

### Compatibility tests

The compatibility tests use [govuk-frontend-diff](https://github.com/matthew-shaw/govuk-frontend-diff) to compare rendered output with GOV.UK Frontend. The simplest way to run them locally is:

```bash
./test.sh
```

This requires Docker. The test image starts the Flask app in `tests/utils/app.py` and runs the comparison tool.

To run the test server and comparison tool directly instead, install `govuk-frontend-diff` and start the Flask server in one terminal:

```bash
(cd tests/utils && uv run --project ../.. --locked python -m flask run --port 3000)
```

Then, in another terminal, run the comparison against the GOV.UK Frontend version configured in CI:

```bash
govuk-frontend-diff http://localhost:3000 --govuk-frontend-version=v6.5.1 --exclude page-template --ci
```

The workflow's Python matrix tests on Python 3.11, 3.12, 3.13, and 3.14. Run checks locally on the version relevant to your change when possible.

### Build the package

Build the source distribution and wheel with:

```bash
uv build --no-sources
```

## Open a pull request

1. Fork the repository if you do not have write access, and make your changes on a branch.
2. Run the relevant lint, compatibility tests, and package build. Mention any checks you could not run and why.
3. Open a [pull request](https://github.com/LandRegistry/govuk-frontend-jinja/compare) with a clear summary, rationale, and test results. Link any related issue.
4. Respond to review feedback and update the pull request as needed. A maintainer will review it and may ask for more information or suggest next steps.

## Versioning and releases

The project uses [Semantic Versioning](https://semver.org/). See the [repository tags](https://github.com/LandRegistry/govuk-frontend-jinja/tags) for published versions.

After an approved change has been merged, a maintainer can create a release and tag following Semantic Versioning. Publishing a GitHub release triggers the workflow that builds the package and publishes it to [PyPI](https://pypi.org/project/govuk-frontend-jinja/); check the project page to confirm the release is available.
