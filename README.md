# GOV.UK Frontend Jinja Macros

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
