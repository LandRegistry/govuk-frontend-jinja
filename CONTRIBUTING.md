# How to contribute

The following are some guidelines to help you make a valuable contribution to this project quicker and easier.

There are two main types of contribution that we welcome; issues and pull requests.

## Create an issue

If you want to raise a bug report to help us improve, or a feature request to suggest an idea for the project, then follow these guidelines:

1. Check the [current issues](https://github.com/LandRegistry/govuk-frontend-jinja/issues) first to see if anyone else has already found the same issue/bug or suggested the same feature/enhancement. If they have, please add a comment to the existing issue to help us understand the scale, impact or demand for that change.

2. If your contribution is not already covered in an existing issue, please [create a new bug report or feature request](https://github.com/LandRegistry/govuk-frontend-jinja/issues/new/choose) using the appropriate issue templates. Please fill out as much of the template as possible to help us understand the details.

3. Your new issue will be reviewed by one of the project maintainers, who may ask for more detail, suggest another course of action, or prioritise and allocate it to a future milestone.

## Create a pull request

If you want to contribute code directly to the project in order to fix a bug or add a feature, then follow these guidelines:

1. Check the [current issues](https://github.com/LandRegistry/govuk-frontend-jinja/issues) and [pull requests](https://github.com/LandRegistry/govuk-frontend-jinja/pulls) first to see if anyone else is already working on the same bug or feature. If they are, consider contributing to that existing issue or pull request first, rather than duplicating work.

2. If your proposed contribution is a new one, please [create a fork](https://guides.github.com/activities/forking/) of the repositiory.

3. Make your contributions to your fork and ensure that the build pipeline still passes. This includes checking dependencies are up-to-date and clear of any security vulnerabilities, running code linting and running unit tests. See the [GitHub workflows](.github/workflows) for details of exactly what the build pipeline will run.

4. Format your Python code with [Black](https://pypi.org/project/black/) using `black . -l 120` for consistency with the existing codebase.

5. If the build passes, [create a pull request](https://guides.github.com/activities/forking/#making-a-pull-request). Please provide as much useful information about your change as possible.

6. Your new pull request will be reviewed by one of the project maintainers, who may ask for more detail, suggest another course of action, or prioritise and allocate it to a future milestone.
