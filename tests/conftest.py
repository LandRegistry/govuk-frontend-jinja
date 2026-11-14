import pytest
from flask.testing import FlaskClient

from tests.utils.app import app


@pytest.fixture(name="client")
def client_fixture() -> FlaskClient:
    return app.test_client()
