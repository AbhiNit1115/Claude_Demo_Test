from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser_client):
        self.browser_client = browser_client
        self.driver = browser_client.driver
        self.wait = browser_client.explicit_wait

    def find_element(self, locator, wait_time: int = None):
        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = self.wait
        return wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator, wait_time: int = None):
        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = self.wait
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text: str, clear_first: bool = True):
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        element = self.find_element(locator)
        return element.text

    def wait_for_text(self, locator, text: str, wait_time: int = None):
        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = self.wait
        wait.until(EC.text_to_be_present_in_element(locator, text))

    def is_element_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def wait_for_element_to_disappear(self, locator, wait_time: int = None):
        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = self.wait
        wait.until(EC.invisibility_of_element_located(locator))
