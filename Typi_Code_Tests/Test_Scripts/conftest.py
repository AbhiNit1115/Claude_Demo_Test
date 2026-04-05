import pytest
from libraries.api_functions.client import ApiClient
from libraries.api_functions.API_Typicode_Functions import TypiCodeAPI

@pytest.fixture(scope='session')
def api_client():
    """
    Provides a session-scoped API client for tests.
    Uses the URL_API environment variable from pytest.ini.
    """
    client = ApiClient('URL_API')
    yield client

@pytest.fixture(scope='session')
def typicode(api_client):
    """
    Provides a session-scoped TypiCode API wrapper for tests.
    """
    api = TypiCodeAPI(api_client)
    yield api

@pytest.fixture(scope='function', autouse=True)
def setup(request):
    """
    Prints the test path at the start of each test.
    """
    path = request.node.nodeid
    print("Starting test: ", path)