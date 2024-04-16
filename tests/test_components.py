import glob
import json
import re

import pytest
from lxml import html
from xmldiff.main import diff_trees


GOVUK_COMPONENTS_TEMPLATES_DIR = "govuk_frontend_jinja/templates/components"
GOVUK_COMPONENTS_NODE_DIR = "node_modules/govuk-frontend/dist/govuk/components"


def get_jinja_components():
    paths = glob.glob(f"{GOVUK_COMPONENTS_TEMPLATES_DIR}/*/macro.html")
    for path in paths:
        component_name = path.split("/")[3]

        yield (component_name)


def get_nunjucks_components():
    paths = glob.glob(f"{GOVUK_COMPONENTS_NODE_DIR}/*/macro.njk")
    for path in paths:
        component_name = path.split("/")[5]

        yield (component_name)


def get_component_fixtures():
    component_fixtures_dict = {}

    for component_name in get_nunjucks_components():
        component_fixtures_dict[component_name] = {}

        with open(f"{GOVUK_COMPONENTS_NODE_DIR}/{component_name}/fixtures.json") as file:
            fixtures = json.load(file)

        for fixture in fixtures.get("fixtures"):
            component_fixtures_dict[component_name][fixture["name"]] = {
                "options": fixture.get("options", {}),
                "html": fixture.get("html", ""),
            }

    return component_fixtures_dict


def components_fixtures():
    fixtures = get_component_fixtures()

    for component_name in get_jinja_components():
        for fixture_name in fixtures[component_name]:
            yield (component_name, fixture_name)


def single_component_fixtures(component_name):
    for fixture_name in get_component_fixtures()[component_name]:
        yield (component_name, fixture_name)


def component_name_to_macro_name(component_name: str):
    return component_name.replace("-", " ").title().replace(" ", "")


def component_fixture(fixtures, component_name, fixture_name):
    fixture = fixtures[component_name][fixture_name]

    return (fixture["options"], fixture["html"])


# For help formatting the HTML to make it compareable
REGEX_REPLACERS = [
    (r"\s{2,}", ""),
    (r"\n", ""),
]


def html_to_one_line(html: str):
    for replacer in REGEX_REPLACERS:
        html = re.sub(*replacer, html)

    return html


def assert_generated_html_matches_fixture(response, component_name, fixture_name, fixture_html):
    assert response.status_code == 200

    fixture_html_string = html_to_one_line(fixture_html)
    macro_html_string = html_to_one_line(response.get_data().decode("utf-8"))

    if not fixture_html_string or not macro_html_string:
        diff = fixture_html_string != macro_html_string
    else:
        fixture_document = html.fromstring(fixture_html_string)
        macro_document = html.fromstring(macro_html_string)

        diff = diff_trees(fixture_document, macro_document)

    assert not diff, f"Did not match for '{component_name}' component with example: '{fixture_name}'"


@pytest.fixture(scope="session")
def component_fixtures():
    return get_component_fixtures()


@pytest.mark.parametrize("component_name, fixture_name", components_fixtures())
def test_render_component(client, component_fixtures, component_name, fixture_name):
    macro_name = component_name_to_macro_name(component_name)
    fixture_options, fixture_html = component_fixture(component_fixtures, component_name, fixture_name)

    response = client.post(
        f"/component/{component_name}",
        content_type="application/json",
        data=json.dumps({"macro_name": macro_name, "params": fixture_options}),
    )
    assert_generated_html_matches_fixture(response, component_name, fixture_name, fixture_html)


def test_all_jinja_templates_exist():
    jinja_components = [component for component in get_jinja_components()]

    nunjucks_components = [component for component in get_nunjucks_components()]

    assert jinja_components == nunjucks_components


# # Debugging test case for testing one component
# @pytest.mark.parametrize("component_name, fixture_name", single_component_fixtures(""))
# def test_component(client, component_fixtures, component_name, fixture_name):
#     macro_name = component_name_to_macro_name(component_name)
#     fixture_options, fixture_html = component_fixture(component_fixtures, component_name, fixture_name)

#     response = client.post(
#         f"/component/{component_name}",
#         content_type="application/json",
#         data=json.dumps({"macro_name": macro_name, "params": fixture_options}),
#     )
#     assert_generated_html_matches_fixture(response, component_name, fixture_name, fixture_html)


# # Debugging test case for testing one component fixture
# def test_individual_component(client, component_fixtures):
#     component_name = ""
#     fixture_name = ""
#     macro_name = component_name_to_macro_name(component_name)
#     fixture_options, fixture_html = component_fixture(component_fixtures, component_name, fixture_name)

#     response = client.post(
#         f"/component/{component_name}",
#         content_type="application/json",
#         data=json.dumps({"macro_name": macro_name, "params": fixture_options}),
#     )
#     assert response.status_code == 200
#     print("---TEST---")
#     print(html_to_one_line(fixture_html))
#     print(html_to_one_line(response.get_data().decode("utf-8")))
#     assert_generated_html_matches_fixture(response, component_name, fixture_name, fixture_html)
