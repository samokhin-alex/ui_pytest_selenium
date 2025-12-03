from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from .locators_page import MainPageLocators


class MainPage(BasePage):

    def should_be_inventory_list(self):
        assert self.is_element_visible(MainPageLocators.INVENTORY_LIST), 'Список товаров отсутствует'

    def should_be_item_images(self):
        items = self.driver.find_elements(*MainPageLocators.INVENTORY_ITEMS)
        assert items, 'На странице нет ни одного товара'

        for index, item in enumerate(items):
            img = item.find_element(*MainPageLocators.INVENTORY_ITEM_IMAGES)
            src = img.get_attribute("src")

            assert src and src.strip() != '', f'У товара #{index + 1} отсутствует или пустой src у картинки'

    def should_be_correct_prices(self, index, expected_price):
        elements_price = self.driver.find_elements(*MainPageLocators.INVENTORY_ITEM_PRICES)
        assert elements_price[index].text == expected_price, f'Не совпадает цена товара. Должна быть {expected_price}'

    def should_be_empty_cart(self):
        cart = self.driver.find_element(*MainPageLocators.CART)
        badges = cart.find_elements(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        assert len(badges) == 0, f"Корзина не пуста! Обнаружен бейдж с количеством: {badges[0].text}"

    def add_1_item_to_cart_button(self):
        buttons = self.driver.find_elements(*MainPageLocators.ADD_TO_CART_BUTTONS)
        buttons[0].click()
        time.sleep(0.5)
        buttons = self.driver.find_elements(*MainPageLocators.REMOVE_FROM_CART_BUTTONS)
        assert buttons[0].text == 'Remove', f'Кнопка добавления в корзину не изменила названия. Ожидалось "Remove", получено "{buttons[0].text}"'

    def add_all_item_to_cart_button(self):
        buttons = self.driver.find_elements(*MainPageLocators.ADD_TO_CART_BUTTONS)
        for button in buttons:
            button.click()

    def get_cart_count(self):
        try:
            cart = self.driver.find_element(*MainPageLocators.CART)
            badge = cart.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
            if badge.is_displayed():
                return int(badge.text)
        except:
            pass
        return 0

    def should_be_added_item_to_cart(self, expected_count):
        actual_count = self.get_cart_count()
        assert actual_count == expected_count, \
            f'В корзине должно быть {expected_count} товаров, а там {actual_count}'
        print(f"✓ В корзине {actual_count} товаров (ожидалось {expected_count})")

