import pytest
from bs4 import BeautifulSoup
from flask.testing import FlaskClient

from tests.govuk_frontend import GovukFrontendPackage

GOVUK_FRONTEND_PACKAGE = GovukFrontendPackage()
GOVUK_FRONTEND_PACKAGE.download_package()


@pytest.mark.parametrize(
    "component,options,html",
    [
        pytest.param(
            component["component"],
            fixture["options"],
            fixture["html"],
            id=f"{component['component']}-{fixture['name']}",
        )
        for component in GOVUK_FRONTEND_PACKAGE.get_all_component_fixtures()
        for fixture in component["fixtures"]
    ],
)
def test_components(client: FlaskClient, component: str, options: dict[list[dict[str, str]]], html: str) -> None:
    response = client.post(f"/component/{component}", json={"macro_name": _to_title(component), "params": options})

    jinja_html = BeautifulSoup(response.text, "html.parser").prettify()
    expected_html = BeautifulSoup(html, "html.parser").prettify()
    assert jinja_html == expected_html


def _to_title(text):
    if "-" in text:
        words = text.split("-")
        return "".join([word.title() for word in words])
    else:
        return text.title()
