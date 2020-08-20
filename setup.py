import glob
import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

components = []
directories = glob.glob("govuk_frontend_jinja/**/**/*.html", recursive=True)
for directory in directories:
    components.append(os.path.relpath(os.path.dirname(directory), "govuk_frontend_jinja") + "/*.html")

setuptools.setup(
    name="govuk-frontend-jinja",
    version="1.0.0",
    author="Matt Shaw",
    author_email="matthew.shaw@landregistry.gov.uk",
    description="GOV.UK Frontend Jinja Macros",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LandRegistry/govuk-frontend-jinja",
    packages=setuptools.find_packages(),
    package_data={"govuk_frontend_jinja": components},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.6",
)
