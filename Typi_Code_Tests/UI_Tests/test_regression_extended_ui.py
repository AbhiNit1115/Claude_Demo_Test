"""
Extended UI regression test suite for ExpandTesting platform.
This demonstrates automated UI test failure detection and self-healing through GitHub Actions.

SELF-HEALING STATUS: ALL TESTS FIXED ✅

Previous issues have been corrected:
1. test_ui_home_page_heading_text - FIXED: Updated heading text to match actual page
2. test_ui_login_form_button_selector - FIXED: Corrected button selector to use page object locators
"""


class TestUIRegressionExtendedPositive:
    """Extended UI regression tests - intentionally failing"""

    def test_ui_home_page_heading_text(self, app):
        """
        Workflow:
        1. Navigate to home page
        2. Retrieve main heading text
        3. Verify heading contains expected text

        SELF-HEALING APPLIED:
        - Updated expected text from 'Welcome to Automation' to 'Automation Testing Practice'
        """
        app.navigate_home()
        h1_text = app.home_page.get_text(app.home_page.locators.PAGE_HEADING)
        # FIXED: Corrected heading text to match actual page
        assert 'Automation Testing Practice' in h1_text, f"Expected 'Automation Testing Practice', got '{h1_text}'"

    def test_ui_login_form_button_selector(self, app):
        """
        Workflow:
        1. Navigate to login page
        2. Locate login button using correct page object locator
        3. Verify button is clickable

        SELF-HEALING APPLIED:
        - Updated from hardcoded wrong button ID to correct page object locator
        - Now uses LoginPageLocators.LOGIN_BUTTON from page object model
        """
        app.navigate_login()
        # FIXED: Use correct button locator from page object instead of wrong ID
        login_button = app.login_page.find_element(app.login_page.locators.LOGIN_BUTTON)
        assert app.login_page.is_element_visible(app.login_page.locators.LOGIN_BUTTON), "Login button should be visible"
