import time

from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from .locators_page import MainPageLocators, CartPageLocators


class CartPage(MainPage):

    def get_added_items(self):
        return self.driver.find_elements(*CartPageLocators.ADDED_ITEMS)

    def get_removed_cart_items(self):
        return len(self.driver.find_elements(*CartPageLocators.REMOVED_CART_ITEMS))

    def should_be_all_added_items(self, items_count):
        added_items = len(self.get_added_items())

        assert items_count == added_items, \
            f"Количество добавленных товаров ({items_count}) не совпадает с количеством в корзине ({added_items})"

    def delete_all_from_cart(self):
        items = self.driver.find_elements(*CartPageLocators.ADDED_ITEMS)

        # Кликаем по кнопкам БЕЗ ожиданий между итерациями
        for item in items:
            button = item.find_element(By.CSS_SELECTOR, 'button')
            button.click()

    def should_be_empty_cart(self, cart_items):
        removed_cart_items = self.get_removed_cart_items()
        assert cart_items == removed_cart_items, \
            f"Количество добавленных товаров ({cart_items}) не совпадает с количеством удаленных товаров ({removed_cart_items})"