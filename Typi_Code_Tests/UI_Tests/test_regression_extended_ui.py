"""
Extended UI regression test suite for ExpandTesting platform.
This demonstrates automated UI test failure detection and self-healing through GitHub Actions.

SELF-HEALING STATUS: INTENTIONALLY FAILING - Ready for demonstration ⚠️

These tests are intentionally designed to fail with specific issues:
1. test_ui_home_page_heading_text - Wrong assertion value
2. test_ui_login_form_button_selector - Incorrect button selector
"""


class TestUIRegressionExtendedPositive:
    """Extended UI regression tests - intentionally failing"""

    def test_ui_home_page_heading_text(self, app):
        """
        Workflow:
        1. Navigate to home page
        2. Retrieve main heading text
        3. Verify heading contains expected text

        SELF-HEALING NEEDED:
        - Current: expects 'Welcome to Automation' (wrong text)
        - Should be: 'Automation Testing Practice' (actual page heading)
        """
        app.navigate_home()
        h1_text = app.home_page.get_text(app.home_page.locators.PAGE_HEADING)
        # BUG: Wrong heading text - page has "Automation Testing Practice" not "Welcome to Automation"
        assert 'Welcome to Automation' in h1_text, f"Expected 'Welcome to Automation', got '{h1_text}'"

    def test_ui_login_form_button_selector(self, app):
        """
        Workflow:
        1. Navigate to login page
        2. Locate login button by CSS selector
        3. Verify button is clickable

        SELF-HEALING NEEDED:
        - Current: using wrong button ID selector (element_not_found)
        - Should be: use correct button locator from page object
        """
        app.navigate_login()
        # BUG: Wrong button ID selector - this element doesn't exist
        login_button = app.login_page.find_element(('id', 'wrong-button-id'))
        assert app.login_page.is_element_visible(('id', 'wrong-button-id')), "Login button should be visible"
