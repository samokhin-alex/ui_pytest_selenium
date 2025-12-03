from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from typing import Tuple

class BasePage():
    def __init__(self, driver, url, timeout=10):
        self.url = url
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, 10)

    def open_url(self):
        self.driver.get(self.url)

    def is_element_present(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def is_element_visible(self, locator: Tuple[str, str], timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def wait_for_element(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator: Tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_disappear(self, locator, timeout = 5):
        try:
            WebDriverWait(self.driver, timeout = 5).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Timeout: Element {locator} did not disappear within {timeout} seconds")
            return False

    def type_text(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_clickable(self, locator, timeout=None):
        try:
            return WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            return False

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def scroll_to_element(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
