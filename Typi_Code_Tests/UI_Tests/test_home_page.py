import pytest


class TestHomePagePositive:
    """Positive test cases for home page"""

    def test_home_page_loads(self, app):
        """Test that home page loads and displays main heading"""
        app.navigate_home()
        app.verify_home_page_structure()

    def test_home_page_h1_heading_text(self, app):
        """Test that H1 heading contains expected text"""
        app.navigate_home()
        h1_text = app.home_page.get_h1_text()
        assert 'Automation Testing Practice' in h1_text

    def test_navigation_links_visible(self, app):
        """Test that all navigation links are visible on home page"""
        app.navigate_home()
        assert app.home_page.is_tips_link_visible()
        assert app.home_page.is_test_cases_link_visible()
        assert app.home_page.is_about_link_visible()

    def test_nav_container_visible(self, app):
        """Test that navigation container is visible"""
        app.navigate_home()
        assert app.home_page.is_nav_container_visible()


class TestHomePageNegative:
    """Negative test cases for home page"""

    def test_invalid_navigation_link_click(self, app):
        """Test that clicking non-existent link raises appropriate error"""
        app.navigate_home()
        from selenium.webdriver.common.by import By
        invalid_locator = (By.XPATH, "//a[@href='/nonexistent']")
        with pytest.raises(Exception):
            app.home_page.wait_for_element_to_disappear(invalid_locator, wait_time=2)


class TestLoginPagePositive:
    """Positive test cases for login page"""

    def test_login_page_loads(self, app):
        """Test that login page loads and displays form"""
        app.navigate_login()
        app.verify_login_page_structure()

    def test_login_form_elements_visible(self, app):
        """Test that all login form elements are visible"""
        app.navigate_login()
        assert app.login_page.is_login_form_visible()
        assert app.login_page.is_username_input_visible()
        assert app.login_page.is_password_input_visible()
        assert app.login_page.is_login_button_visible()

    def test_login_with_valid_credentials(self, app):
        """Test login with valid test credentials"""
        app.navigate_login()
        app.login_page.login('practice', 'SuperSecretPassword!')
        import time
        time.sleep(2)


class TestLoginPageNegative:
    """Negative test cases for login page"""

    def test_login_with_invalid_credentials(self, app):
        """Test login with invalid credentials"""
        app.navigate_login()
        app.login_page.login('invalid_user', 'invalid_password')
        import time
        time.sleep(2)

    def test_login_with_empty_username(self, app):
        """Test login with empty username"""
        app.navigate_login()
        app.login_page.login('', 'password')
        import time
        time.sleep(1)

    def test_login_with_empty_password(self, app):
        """Test login with empty password"""
        app.navigate_login()
        app.login_page.login('username', '')
        import time
        time.sleep(1)


class TestPageNavigation:
    """Test page navigation flows"""

    def test_navigate_home_to_login(self, app):
        """Test navigation from home page to login page"""
        app.navigate_home()
        app.verify_home_page_structure()
        app.navigate_login()
        app.verify_login_page_structure()

    def test_navigate_login_to_home(self, app):
        """Test navigation from login page back to home"""
        app.navigate_login()
        app.verify_login_page_structure()
        app.navigate_home()
        app.verify_home_page_structure()
