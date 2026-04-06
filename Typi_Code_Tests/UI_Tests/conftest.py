import pytest
import os
from libraries.ui_functions.browser_client import BrowserClient
from libraries.ui_functions.ui_application import UIApplication


@pytest.fixture(scope='session')
def browser_client():
    """
    Provides a session-scoped BrowserClient for tests.
    Uses the BASE_URL environment variable from pytest.ini.
    Cleans up the driver after all tests.
    """
    client = BrowserClient('BASE_URL', 'BROWSER')
    yield client
    client.quit()


@pytest.fixture(scope='session')
def app(browser_client):
    """
    Provides a session-scoped UIApplication wrapper for tests.
    """
    application = UIApplication(browser_client)
    yield application


@pytest.fixture(scope='function', autouse=True)
def setup(request, app):
    """
    Prints test name at start.
    """
    path = request.node.nodeid
    print(f"\nStarting test: {path}")


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call
