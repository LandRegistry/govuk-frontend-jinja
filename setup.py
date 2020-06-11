import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="govuk-frontend-jinja",
    version="0.0.1",
    author="Matt Shaw",
    author_email="matthew.shaw@landregistry.gov.uk",
    description="GOV.UK Frontend Jinja Macros",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LandRegistry/govuk-frontend-jinja",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
