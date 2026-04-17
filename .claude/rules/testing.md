# Testing Rules and Standards

This file documents testing conventions and standards for this project. These rules ensure consistency across all test suites.

## Test Naming Conventions

- **All test case names** must start with `test_`
- **All API test cases** must be prefixed with `test_api_`
- **All UI test cases** must be prefixed with `test_ui_`

### Examples

**API Tests:**
```python
def test_api_get_posts(typicode):
    """Valid: follows test_api_ convention"""
    pass

def test_api_invalid_endpoint_error_handling(typicode):
    """Valid: descriptive name with api_ prefix"""
    pass
```

**UI Tests:**
```python
def test_ui_home_page_loads(app):
    """Valid: follows test_ui_ convention"""
    pass

def test_ui_login_form_validation(app):
    """Valid: descriptive name with ui_ prefix"""
    pass
```

**Invalid:**
```python
def api_get_posts(typicode):
    """Invalid: missing test_ prefix"""
    pass

def test_home_page(app):
    """Invalid: missing ui_ prefix for UI test"""
    pass
```

## Test Structure

All test scripts must include a **Workflow Section** that describes the test flow:

```python
def test_ui_login_success(app):
    """
    Workflow:
    1. Navigate to login page
    2. Enter valid credentials
    3. Verify successful login and redirect to dashboard
    """
    app.navigate_login()
    app.login_page.enter_credentials("practice", "SuperSecretPassword!")
    app.verify_login_success()
```

```python
def test_api_get_posts(typicode):
    """
    Workflow:
    1. Send GET request to /posts endpoint
    2. Verify response structure contains required fields
    3. Validate post count equals 100
    4. Confirm all post IDs are unique
    """
    typicode.get_posts()
    typicode.verify_posts_structure()
    typicode.verify_post_count(100)
    typicode.verify_post_ids_unique()
```

## Test Organization

- **Positive tests**: Test expected behavior and successful workflows
- **Negative tests**: Test error handling, validation, and edge cases
- **Test classes**: Group related tests into classes for better organization

Example:
```python
class TestLoginPagePositive:
    """Positive test cases for login page"""
    
    def test_ui_login_success(self, app):
        pass

class TestLoginPageNegative:
    """Negative test cases for login page"""
    
    def test_ui_login_invalid_credentials(self, app):
        pass
```

## Fixture Usage

- Use fixtures provided in `conftest.py`
- API tests: `typicode` fixture (session-scoped)
- UI tests: `app` fixture (session-scoped)
- Avoid creating duplicate fixtures

## Verification Methods

Tests should leverage verification methods from API/UI wrapper classes:

**API:**
- `verify_posts_structure()`: Check required keys
- `verify_post_count()`: Check response size
- `verify_post_ids_unique()`: Check uniqueness
- `verify_user_id_range()`: Check value ranges

**UI:**
- `verify_home_page_structure()`: Check home page elements
- `verify_login_page_structure()`: Check login form elements
- `is_element_visible()`: Check visibility
- `wait_for_text()`: Wait for specific text

## Test Location

- **API Tests**: `Typi_Code_Tests/Test_Scripts/test_*.py`
- **UI Tests**: `Typi_Code_Tests/UI_Tests/test_*.py`
