# code-quality

Analyze and provide guidance on code quality issues in the repository. This skill identifies problems and suggests fixes without making destructive changes.

## ⚠️ Tool Restrictions (Analysis-Only Mode)

**Allowed Tools:**
- `Read`: Read files
- `Glob`: Search for files
- `Grep`: Search file contents
- `Agent`: Run code analysis
- `Write`: Create analysis reports only

**Blocked Tools:**
- `Bash`: No command execution (prevents accidental `rm`, `git push --force`, etc.)
- `Edit`: No file modification during analysis
- `TaskCreate/TaskStop`: No task management

## Features

- **Issue Detection**: Scans for code quality problems including:
  - Code duplication (DRY violations)
  - Missing or incomplete type hints
  - Hardcoded magic values
  - Inconsistent docstrings
  - Broad exception handling
  - Import issues
  - Performance inefficiencies
  - Unused code

- **Severity Levels**:
  - 🔴 **HIGH**: Major issues affecting maintainability or functionality
  - 🟡 **MEDIUM**: Important issues that should be addressed
  - 🟢 **LOW**: Minor issues or optimization opportunities

## Usage

```
/code-quality              # Full codebase analysis
/code-quality api          # Analyze API layer only
/code-quality ui           # Analyze UI layer only
/code-quality tests        # Analyze test files only
/code-quality summary      # Quick summary of top 10 issues
```

## Known Issues

### 🔴 HIGH PRIORITY

1. **Duplicate Code Blocks** - DRY Violation
   - Location: `browser_client.py` and `base_page.py`
   - Issue: `find_element()` and `find_elements()` are duplicated
   - Fix: Extract to shared utility or base class
   - Impact: Maintenance burden, inconsistent behavior

2. **Hardcoded Magic Values** - No Constants
   - Location: `API_Typicode_Functions.py`
   - Issue: Expected count (100), ranges (1-10) hardcoded
   - Fix: Extract to class constants like `EXPECTED_POST_COUNT`
   - Impact: Difficult to maintain and test

3. **Missing Type Hints on Locators** - Type Safety
   - Location: `base_page.py`, `browser_client.py`
   - Issue: `locator` parameter lacks type hints (should be `Tuple[By, str]`)
   - Fix: Add type hints to all locator parameters and returns
   - Impact: IDE autocomplete fails, type checking disabled

4. **time.sleep() Instead of Explicit Waits** - Test Flakiness
   - Location: `test_home_page.py` test methods
   - Issue: Using blocking delays instead of Selenium waits
   - Fix: Replace with `wait_for_element()`, `wait_for_text()`, etc.
   - Impact: Tests are slow and unreliable

### 🟡 MEDIUM PRIORITY

5. **Unused Imports**
   - Location: `base_page.py` line 3 (`Keys` from selenium)
   - Fix: Remove unused import
   - Impact: Code cleanliness

6. **Broad Exception Handling**
   - Location: `client.py`, `base_page.py`, `typicode_api.py`
   - Issue: `except Exception:` catches too much
   - Fix: Catch specific exceptions (`TimeoutException`, `NoSuchElementException`, etc.)
   - Impact: Masks errors, makes debugging harder

7. **Missing Return Type Hints**
   - Location: `ui_application.py`, `browser_client.py`
   - Issue: Methods lack return type annotations
   - Fix: Add explicit return types (e.g., `-> WebElement`, `-> bool`)
   - Impact: Type checking incomplete, IDE hints missing

8. **Inconsistent Docstring Style**
   - Location: Various files
   - Issue: Some functions have docstrings, others don't; no consistent style
   - Fix: Use Google style docstrings with parameter documentation
   - Impact: Unclear API contracts

9. **Incorrect Import Path**
   - Location: `typicode_api.py` line 1
   - Issue: `from client import ApiClient` won't work
   - Fix: Use `from libraries.api_functions.client import ApiClient`
   - Impact: Runtime import failure

### 🟢 LOW PRIORITY

10. **Inefficient Algorithm**
    - Location: `API_Typicode_Functions.py` - `verify_post_ids_unique()`
    - Issue: O(n²) nested loop for uniqueness check
    - Fix: Use set-based approach for O(n) complexity
    - Impact: Performance on large datasets

## Analysis Commands

When using this skill, only **read and write operations** are allowed to prevent accidental destructive changes:

✅ **Allowed:**
- Read files (`Read` tool)
- Write/create files (`Write` tool)
- Search files (`Grep` tool)
- List files (`Glob` tool)

❌ **Not Allowed:**
- Delete files or directories
- Force push or destructive git operations
- Execute bash commands that modify system state
- Install/remove packages

## Example Fixes

### Fix: Add Type Hints

```python
# Before
def find_element(self, locator):
    return self.driver.find_element(*locator)

# After
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def find_element(self, locator: Tuple[By, str]) -> WebElement:
    return self.driver.find_element(*locator)
```

### Fix: Extract Magic Values

```python
# Before
def verify_post_count(self, expected_count: int = 100) -> None:
    if len(self.last_response) != expected_count:
        raise AssertionError(f"Expected {expected_count} posts")

# After
class TypiCodeAPI:
    EXPECTED_POST_COUNT = 100
    MIN_USER_ID = 1
    MAX_USER_ID = 10
    
    def verify_post_count(self, expected_count: int = None) -> None:
        expected_count = expected_count or self.EXPECTED_POST_COUNT
        if len(self.last_response) != expected_count:
            raise AssertionError(f"Expected {expected_count} posts")
```

### Fix: Remove time.sleep()

```python
# Before
def test_login_with_valid_credentials(self, app):
    app.navigate_login()
    time.sleep(2)  # ❌ Brittle delay
    app.login_page.enter_credentials("practice", "SuperSecretPassword!")
    time.sleep(3)
    assert app.is_login_successful()

# After
def test_ui_login_success(self, app):
    """
    Workflow:
    1. Navigate to login page
    2. Wait for login form to appear
    3. Enter credentials
    4. Wait for success confirmation
    """
    app.navigate_login()
    app.login_page.wait_for_username_field()  # ✅ Explicit wait
    app.login_page.enter_credentials("practice", "SuperSecretPassword!")
    app.verify_login_success()  # ✅ Wait built-in
```

## How to Use This Skill

1. Run `/code-quality` to see full analysis
2. Pick **one HIGH priority issue** to fix
3. Reference the example fixes above
4. Make changes using `Write` tool
5. Run `/run-tests` to verify fixes don't break tests
6. Repeat for other issues

## Notes

- This skill provides analysis and guidance only
- No automated fixes are applied to preserve code ownership
- Always run tests after making changes
- Focus on HIGH priority issues first, then MEDIUM, then LOW
- Reference CLAUDE.md for code style guidelines
