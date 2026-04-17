import os
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BrowserClient:
    def __init__(self, base_url_env: str = 'BASE_URL', browser_env: str = 'BROWSER'):
        self.base_url = os.getenv(base_url_env)
        if not self.base_url:
            raise ValueError(f"Environment variable '{base_url_env}' not set.")

        browser_type = os.getenv(browser_env, 'chrome').lower()
        explicit_wait = int(os.getenv('EXPLICIT_WAIT', 10))
        implicit_wait = int(os.getenv('IMPLICIT_WAIT', 5))

        if browser_type == 'chrome':
            self.driver = self._create_chrome_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

        self.driver.implicitly_wait(implicit_wait)
        self.explicit_wait = WebDriverWait(self.driver, explicit_wait)
        self.correlation_id = str(uuid.uuid4())

    def _create_chrome_driver(self):
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Enable headless mode for CI/CD environments or when explicitly requested
        is_headless = os.getenv('CI') or os.getenv('BROWSER', '').lower() == 'chrome_headless'
        if is_headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')

        # Use webdriver-manager to automatically handle ChromeDriver
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def navigate(self, path: str = '') -> None:
        url = self.base_url + path
        self.driver.get(url)

    def find_element(self, locator, wait_time: int = None):
        if wait_time:
            wait = WebDriverWait(self.driver, wait_time)
        else:
            wait = self.explicit_wait
        return wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def take_screenshot(self, filename: str) -> None:
        self.driver.save_screenshot(filename)

    def quit(self) -> None:
        if self.driver:
            self.driver.quit()
