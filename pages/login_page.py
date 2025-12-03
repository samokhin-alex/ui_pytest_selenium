from pages.base_page import BasePage
from .locators_page import LoginPageLocators
from utils.utils import ReadConfig


class LoginPage(BasePage):

    def should_be_login_link(self):
        assert self.driver.current_url == self.url, f'URL = {self.driver.current_url}, должен быть {self.url}'

    def login(self, username, password):
        self.open_url()
        self.type_text(LoginPageLocators.USER_NAME, username)
        self.type_text(LoginPageLocators.PASSWORD, password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert self.driver.current_url == ReadConfig.get_inventory_url()


