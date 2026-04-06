from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePageLocators:
    H1_HEADING = (By.XPATH, "//h1[contains(text(), 'Automation Testing Practice')]")
    TIPS_LINK = (By.XPATH, "//a[contains(text(), 'Tips')]")
    TEST_CASES_LINK = (By.XPATH, "//a[contains(text(), 'Test Cases')]")
    ABOUT_LINK = (By.XPATH, "//a[contains(text(), 'About')]")
    LOGO_HOME_LINK = (By.XPATH, "//a[@href='/']")
    NAV_CONTAINER = (By.XPATH, "//nav")


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit-login")
    FORM = (By.ID, "login")
    USERNAME_LABEL = (By.XPATH, "//label[@for='username']")
    PASSWORD_LABEL = (By.XPATH, "//label[@for='password']")


class HomePage(BasePage):
    def navigate_to_home(self) -> None:
        self.browser_client.navigate('')

    def navigate_to_login(self) -> None:
        self.browser_client.navigate('/login')

    def get_h1_text(self) -> str:
        return self.get_text(HomePageLocators.H1_HEADING)

    def is_tips_link_visible(self) -> bool:
        return self.is_element_visible(HomePageLocators.TIPS_LINK)

    def is_test_cases_link_visible(self) -> bool:
        return self.is_element_visible(HomePageLocators.TEST_CASES_LINK)

    def is_about_link_visible(self) -> bool:
        return self.is_element_visible(HomePageLocators.ABOUT_LINK)

    def is_nav_container_visible(self) -> bool:
        return self.is_element_visible(HomePageLocators.NAV_CONTAINER)

    def click_tips_link(self) -> None:
        self.click(HomePageLocators.TIPS_LINK)

    def click_test_cases_link(self) -> None:
        self.click(HomePageLocators.TEST_CASES_LINK)

    def click_about_link(self) -> None:
        self.click(HomePageLocators.ABOUT_LINK)

    def verify_home_page_loaded(self) -> None:
        if not self.is_element_visible(HomePageLocators.H1_HEADING):
            raise AssertionError("Home page did not load - H1 heading not found")

    def verify_navigation_visible(self) -> None:
        required_links = [
            HomePageLocators.TIPS_LINK,
            HomePageLocators.TEST_CASES_LINK,
            HomePageLocators.ABOUT_LINK
        ]
        for link in required_links:
            if not self.is_element_visible(link):
                raise AssertionError(f"Navigation link not visible: {link}")


class LoginPage(BasePage):
    def navigate_to_login(self) -> None:
        self.browser_client.navigate('/login')

    def is_login_form_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.FORM)

    def is_username_input_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.USERNAME_INPUT)

    def is_password_input_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.PASSWORD_INPUT)

    def is_login_button_visible(self) -> bool:
        return self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.type_text(LoginPageLocators.USERNAME_INPUT, username)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def verify_login_page_loaded(self) -> None:
        if not self.is_element_visible(LoginPageLocators.FORM):
            raise AssertionError("Login page did not load - form not found")

    def verify_login_form_elements(self) -> None:
        required_elements = [
            LoginPageLocators.USERNAME_INPUT,
            LoginPageLocators.PASSWORD_INPUT,
            LoginPageLocators.LOGIN_BUTTON
        ]
        for element in required_elements:
            if not self.is_element_visible(element):
                raise AssertionError(f"Required login form element not found: {element}")
