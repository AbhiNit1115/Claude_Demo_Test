# run-tests

Run the test suite for the project. Executes both API and UI tests with verbose output.

## ⚠️ Tool Restrictions

**Allowed Tools:**
- `Read`: Read test files and configs
- `Bash`: Execute pytest commands only

**Allowed Bash Commands:**
- `pytest Typi_Code_Tests/`
- `pytest Typi_Code_Tests/Test_Scripts/`
- `pytest Typi_Code_Tests/UI_Tests/`

**Blocked:**
- `rm`, `git push --force`, `pip uninstall` — prevented at execution time

## Usage

```
/run-tests          # Run all tests
/run-tests api      # Run only API tests
/run-tests ui       # Run only UI tests
/run-tests all -v   # Run all tests with verbose output
```

## Commands

```bash
# Run all tests (API + UI)
pytest Typi_Code_Tests/ -v

# Run only API tests
pytest Typi_Code_Tests/Test_Scripts/ -v

# Run only UI tests
pytest Typi_Code_Tests/UI_Tests/ -v

# Run all tests with detailed output (including print statements)
pytest Typi_Code_Tests/ -v -s

# Run specific test file
pytest Typi_Code_Tests/Test_Scripts/test_typi_code_api_details.py -v

# Run specific test
pytest Typi_Code_Tests/Test_Scripts/test_typi_code_api_details.py::test_api_get_posts -v

# Run UI tests in headless mode
BROWSER=chrome_headless pytest Typi_Code_Tests/UI_Tests/ -v

# Generate HTML report
pytest Typi_Code_Tests/ --html=report.html --self-contained-html
```

## Environment Variables

- `BROWSER`: Set to `chrome_headless` for CI/CD environments (default: `chrome`)
- `URL_API`: API endpoint (defined in `Typi_Code_Tests/Test_Scripts/pytest.ini`)
- `BASE_URL`: UI base URL (defined in `Typi_Code_Tests/UI_Tests/pytest.ini`)

## Notes

- Tests are session-scoped, so fixtures are reused across the full run
- All commands should be run from the project root directory
- Use `-s` flag to see print statements and debug output
- UI tests require ChromeDriver to be installed and in PATH
