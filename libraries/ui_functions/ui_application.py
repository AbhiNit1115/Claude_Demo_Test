from libraries.ui_functions.pages.home_page import HomePage, LoginPage


class UIApplication:
    def __init__(self, browser_client):
        self.browser_client = browser_client
        self._home_page = None
        self._login_page = None
        self.last_response = None

    @property
    def home_page(self) -> HomePage:
        if self._home_page is None:
            self._home_page = HomePage(self.browser_client)
        return self._home_page

    @property
    def login_page(self) -> LoginPage:
        if self._login_page is None:
            self._login_page = LoginPage(self.browser_client)
        return self._login_page

    def navigate_home(self) -> None:
        self.home_page.navigate_to_home()

    def navigate_login(self) -> None:
        self.login_page.navigate_to_login()

    def take_screenshot(self, filename: str) -> None:
        self.browser_client.take_screenshot(filename)

    def verify_home_page_structure(self) -> None:
        self.home_page.verify_home_page_loaded()
        self.home_page.verify_navigation_visible()

    def verify_login_page_structure(self) -> None:
        self.login_page.verify_login_page_loaded()
        self.login_page.verify_login_form_elements()
