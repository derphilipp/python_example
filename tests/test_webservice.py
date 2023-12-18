# import pytest
# import requests


# # from python_example.app import app


# @pytest.fixture
# def url():
#     return "http://localhost/hello"


# def test_hello(url):
#     response = requests.get(url)
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World"}


import pytest
import requests

from src.python_example import app as myapp


@pytest.fixture()
def app():
    app = myapp()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def url():
    return "http://localhost/hello"


def test_hello(url):
    response = requests.get(url=url)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
