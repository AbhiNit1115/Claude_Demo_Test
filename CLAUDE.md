# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python testing project for the **TypiCode API** (https://jsonplaceholder.typicode.com/) and **ExpandTesting** UI (https://practice.expandtesting.com/). The project provides an API client framework, UI testing framework, and comprehensive tests with a focus on validating API response structure, data integrity, and UI functionality.

## Setup

### Prerequisites

Requires Python 3.7+ and the following packages:
- `pytest` — Testing framework
- `pytest-env` — Plugin for environment variable management in pytest.ini
- `requests` — HTTP client library
- `selenium>=4.0.0` — WebDriver library for UI testing

Install dependencies:
```bash
pip install -r requirements.txt
```

Or individually:
```bash
pip install pytest pytest-env requests selenium
```

## Architecture

### Core Components

**API Client Layer** (`libraries/api_functions/`)
- `client.py`: Generic HTTP client (`ApiClient`) that wraps `requests.Session` with:
  - Environment variable-based base URL configuration
  - Automatic header management (correlation IDs via UUID)
  - Response error handling (`ResponseError` exception)
  - Verb methods (GET, POST, PUT, PATCH, DELETE) that build full URLs and verify responses

**API Wrapper Layer** (`libraries/api_functions/`)
- `API_Typicode_Functions.py`: Domain-specific wrapper (`TypiCodeAPI`) that:
  - Caches the last API response in `last_response` for use in verification methods
  - Provides verification methods for data integrity (structure, counts, uniqueness, ranges)
  - Implements both positive and negative tests as instance methods
  - Used as a pytest fixture in tests
  - Uses `Endpoints` class for centralized endpoint path management

**Test Infrastructure** (`Typi_Code_Tests/Test_Scripts/`)
- `conftest.py`: Pytest fixtures providing session-scoped API clients:
  - `api_client` — Base HTTP client configured with `URL_API` environment variable
  - `typicode` — TypiCode API wrapper (depends on `api_client`)
  - `setup` — Function-scoped fixture that prints test names at start
- `test_typi_code_api_details.py`: Test suite exercising the API
- `pytest.ini`: Configuration file that loads `URL_API` environment variable via pytest-env plugin

**Utilities**
- `setup/update_pytest_ini.py`: CLI tool to manage pytest.ini configuration and update the `URL_API`

## UI Testing Architecture

### UI Components

**UI Browser Client** (`libraries/ui_functions/browser_client.py`)
- `BrowserClient`: Generic WebDriver wrapper that mirrors `ApiClient`:
  - Initialize Chrome WebDriver with environment-based configuration
  - Manage implicit/explicit waits via Selenium WebDriverWait
  - Navigate to URLs (relative to BASE_URL)
  - Take screenshots for debugging
  - Graceful shutdown

**UI Page Objects** (`libraries/ui_functions/pages/`)
- `base_page.py`: Base class for all page objects with reusable interactions:
  - `find_element()`: Find element with explicit wait
  - `find_elements()`: Find multiple elements
  - `click()`: Click with clickability check
  - `type_text()`: Type text with optional clear
  - `get_text()`: Get element text
  - `is_element_visible()`: Check visibility
  - `wait_for_text()`: Wait for specific text in element
  - `wait_for_element_to_disappear()`: Wait for element to vanish
- `home_page.py`: Specific page objects for expandtesting.com:
  - `HomePage`: Home page with navigation, heading verification
  - `LoginPage`: Login form with username/password inputs, login button
  - `HomePageLocators`: XPath-based locators for home page elements
  - `LoginPageLocators`: ID/XPath-based locators for login form

**UI Application Layer** (`libraries/ui_functions/ui_application.py`)
- `UIApplication`: Domain wrapper mirroring `TypiCodeAPI`:
  - Lazy-loads page objects (home_page, login_page)
  - Caches application state in `last_response`
  - Provides workflow methods (navigate_home, navigate_login)
  - Provides verification methods (verify_home_page_structure, verify_login_page_structure)
  - Delegates screenshot taking to BrowserClient

**UI Test Infrastructure** (`Typi_Code_Tests/UI_Tests/`)
- `conftest.py`: Pytest fixtures providing session-scoped UI components:
  - `browser_client` — BrowserClient configured with BASE_URL environment variable
  - `app` — UIApplication wrapper (depends on browser_client)
  - `setup` — Function-scoped fixture that prints test names
- `test_home_page.py`: Test suite with positive/negative tests for home page and login page
- `pytest.ini`: Configuration file that loads environment variables (BROWSER, BASE_URL, waits) via pytest-env plugin

### Environment Variables (UI Tests)
- `BROWSER`: Browser type (default: 'chrome')
- `BASE_URL`: Base URL for navigation (default: https://practice.expandtesting.com/)
- `EXPLICIT_WAIT`: Explicit wait timeout in seconds (default: 10)
- `IMPLICIT_WAIT`: Implicit wait timeout in seconds (default: 5)

## Development Commands

### Running Tests

All commands should be run from the project root directory:

```bash
# Run all API tests
pytest Typi_Code_Tests/Test_Scripts/

# Run all UI tests
pytest Typi_Code_Tests/UI_Tests/

# Run a specific test class
pytest Typi_Code_Tests/Test_Scripts/test_typi_code_api_details.py::TestClassName

# Run a specific test
pytest Typi_Code_Tests/Test_Scripts/test_typi_code_api_details.py::test_typicode_get_posts

# Run with verbose output
pytest Typi_Code_Tests/Test_Scripts/ -v

# Run with detailed print statements
pytest Typi_Code_Tests/Test_Scripts/ -s

# Run UI tests in headless mode (CI/CD compatible)
BROWSER=chrome_headless pytest Typi_Code_Tests/UI_Tests/ -v

# Generate HTML report
pytest Typi_Code_Tests/ --html=report.html --self-contained-html
```

### Using Fixtures in Tests

Tests receive fixtures through function parameters. Session-scoped fixtures are reused across all tests:

```python
def test_api_example(typicode):
    # typicode is a TypiCodeAPI instance with cached api_client
    typicode.get_posts()
    typicode.verify_posts_structure()

def test_ui_example(app):
    # app is a UIApplication instance with page objects
    app.navigate_home()
    app.verify_home_page_structure()
```

The `api_client` fixture is available directly but typically used through `typicode`.
The `browser_client` fixture is available directly but typically used through `app`.

### Configuration

The `URL_API` environment variable is defined in `Typi_Code_Tests/Test_Scripts/pytest.ini` and loaded by the pytest-env plugin. Update it using the provided utility:

```bash
# Check current API URL
python setup/update_pytest_ini.py

# Update pytest.ini with custom API URL
python setup/update_pytest_ini.py custom https://jsonplaceholder.typicode.com/
```

### Extending Page Objects

Add new page objects to `libraries/ui_functions/pages/`:

```python
class NewPageLocators:
    ELEMENT_ID = (By.ID, "element_id")

class NewPage(BasePage):
    def click_element(self):
        self.click(NewPageLocators.ELEMENT_ID)
```

Then add to `UIApplication`:

```python
@property
def new_page(self) -> NewPage:
    if self._new_page is None:
        self._new_page = NewPage(self.browser_client)
    return self._new_page
```

### Extending API Endpoints

Add new endpoints to the `Endpoints` class in `API_Typicode_Functions.py`:

```python
class Endpoints:
    POSTS = 'posts'
    COMMENTS = 'comments'  # New endpoint
```

Then implement methods in `TypiCodeAPI`:

```python
def get_comments(self) -> List[Dict[str, Any]]:
    response = self.client.get(Endpoints.COMMENTS)
    self.last_response = response
    return response

def verify_comments_structure(self) -> None:
    # Verification logic for comments
    pass
```

### Test Credentials

For ExpandTesting login tests, use these test credentials:
- **Username**: `practice`
- **Password**: `SuperSecretPassword!`

These are defined on the login page itself at https://practice.expandtesting.com/login

## Key Design Patterns

- **Session-scoped fixtures**: API and UI clients are reused across all tests for efficiency
- **Separation of concerns**:
  - ApiClient (HTTP transport) vs TypiCodeAPI (domain logic)
  - BrowserClient (WebDriver transport) vs UIApplication (UI workflows)
- **Response/state caching**: `TypiCodeAPI.last_response` and `UIApplication.last_response` cache state
- **Verification-heavy testing**: Tests focus on structure and data validation rather than behavior
- **Correlation tracking**: Each API request includes a unique UUID correlation ID
- **Environment-based configuration**: URLs and timeouts configured via pytest.ini with pytest-env plugin
- **Lazy page object loading**: Page objects are instantiated on first access, not on fixture creation

## Code Style Guidelines

- Use comments sparingly — only for complex or non-obvious logic
- Prefer clear variable/function names over explanatory comments
- Self-documenting code is preferred

## Testing Standards

Comprehensive testing rules and conventions are maintained in **[`.claude/rules/testing.md`](.claude/rules/testing.md)**.

### Quick Summary

- Test names must follow: `test_api_*` (API), `test_ui_*` (UI)
- All test methods must include a **Workflow section** describing test steps
- Tests are organized in test classes: `TestNamePositive` and `TestNameNegative`
- Use verification methods from `TypiCodeAPI` and `UIApplication` wrappers

For detailed guidelines, conventions, and examples, see **[`.claude/rules/testing.md`](.claude/rules/testing.md)**.
