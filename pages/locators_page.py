from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

class MainPageLocators:
    LOGO_TEXT = (By.CSS_SELECTOR, '[class="header_label"] [class="app_logo"]')
    INVENTORY_LIST = (By.CSS_SELECTOR, '[class="inventory_list"]')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, '[class="inventory_item"]')
    INVENTORY_ITEM_IMAGES = (By.CSS_SELECTOR, '[class="inventory_item_img"] img')
    INVENTORY_ITEM_PRICES = (By.CSS_SELECTOR, '[class="inventory_item_price"]')
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, '[class="btn btn_primary btn_small btn_inventory "]')
    REMOVE_FROM_CART_BUTTONS = (By.CSS_SELECTOR, '[class="btn btn_secondary btn_small btn_inventory "]')
    CART = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')