import pytest
from utils.utils import ReadConfig
from pages.locators_page import MainPageLocators


def test_correct_url(login_page):
    login_page.open_url()
    login_page.should_be_login_link()

def test_login(login_page):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()

    login_page.login(username, password)

def test_inventory_list_visible(main_page, login_page):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()

    login_page.login(username, password)
    main_page.should_be_inventory_list()

def test_check_item_images(main_page, login_page):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()

    login_page.login(username, password)
    main_page.should_be_item_images()

@pytest.mark.parametrize("index, expected_price", [
        (0, "$29.99"),
        (1, "$9.99"),
        (2, "$15.99"),
        (3, "$49.99"),
        (4, "$7.99"),
        (5, "$15.99"),
])
def test_check_prices(main_page, login_page, index, expected_price):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()

    login_page.login(username, password)
    main_page.should_be_correct_prices(index, expected_price)

def test_add_to_cart_1_item(main_page, login_page):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()
    expected_count = 1

    login_page.login(username, password)
    main_page.should_be_empty_cart()
    main_page.add_1_item_to_cart_button()
    main_page.should_be_added_item_to_cart(expected_count)

def test_add_to_cart_all_items(main_page, login_page):
    username = ReadConfig.get_standard_user_login()
    password = ReadConfig.get_standard_user_password()

    login_page.login(username, password)

    expected_count = len(main_page.driver.find_elements(*MainPageLocators.ADD_TO_CART_BUTTONS))

    main_page.should_be_empty_cart()
    main_page.add_all_item_to_cart_button()
    main_page.should_be_added_item_to_cart(expected_count)


