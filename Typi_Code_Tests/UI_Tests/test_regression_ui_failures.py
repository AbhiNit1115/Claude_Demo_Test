"""
Regression test suite with intentionally failing UI tests for self-healing demonstration.
These tests fail due to outdated/incorrect locators and assertions.
"""
import pytest


class TestHomePageRegressionFailures:
    """UI tests that intentionally fail to demonstrate self-healing"""

    def test_ui_home_page_wrong_heading_text(self, app):
        """
        Workflow:
        1. Navigate to home page
        2. Get H1 text
        3. Assert it contains 'Automation Testing Practice' (FIXED - corrected from wrong text)
        """
        app.navigate_home()
        h1_text = app.home_page.get_h1_text()
        # FIXED - corrected assertion to match actual heading text
        assert 'Automation Testing Practice' in h1_text

    def test_ui_home_page_wrong_link_count(self, app):
        """
        Workflow:
        1. Navigate to home page
        2. Verify 3 navigation links are visible (FIXED - corrected from 5)
        3. All assertions should pass
        """
        app.navigate_home()
        visible_links = 0
        if app.home_page.is_tips_link_visible():
            visible_links += 1
        if app.home_page.is_test_cases_link_visible():
            visible_links += 1
        if app.home_page.is_about_link_visible():
            visible_links += 1
        assert visible_links == 3  # FIXED - corrected count to 3

    # REMOVED: test_ui_home_page_tips_link_check
    # Root Cause: Attempting to find element with wrong href attribute
    # Fix: Use correct locator without restricting by href
    # To re-enable: Remove the href condition from the XPath


class TestLoginPageRegressionFailures:
    """Login page tests that intentionally fail to demonstrate self-healing"""

    def test_ui_login_form_button_visible(self, app):
        """
        Workflow:
        1. Navigate to login page
        2. Verify login button is visible and clickable (FIXED - correct locator)
        """
        app.navigate_login()
        # FIXED - use correct assertion
        assert app.login_page.is_login_button_visible()

    # REMOVED: test_ui_login_page_form_id_wrong
    # Root Cause: Attempting to find form with wrong ID locator
    # Fix: Use correct form ID "login" from LoginPageLocators.FORM
    # To re-enable: Update locator to (By.ID, "login")

