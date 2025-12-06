import pytest

from conftest import main_page
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
    login_page.standard_login()
    main_page.should_be_inventory_list()

def test_check_item_images(main_page, login_page):
    login_page.standard_login()
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
    login_page.standard_login()
    main_page.should_be_correct_prices(index, expected_price)

def test_add_to_cart_1_item(main_page, login_page):
    expected_count = 1

    login_page.standard_login()
    main_page.should_be_empty_cart()
    main_page.add_1_item_to_cart()
    main_page.should_be_added_item_to_cart(expected_count)

def test_add_to_cart_all_items(main_page, login_page):
    login_page.standard_login()

    expected_count = len(main_page.driver.find_elements(*MainPageLocators.INVENTORY_ITEMS))

    main_page.should_be_empty_cart()
    main_page.add_all_item_to_cart()
    main_page.should_be_added_item_to_cart(expected_count)

def test_cart_page_is_opened(login_page, cart_page, main_page):
    login_page.standard_login()
    main_page.open_cart()
    main_page.should_be_curt_url()

def test_check_cart_has_all_added_items(main_page, cart_page, login_page):
    login_page.standard_login()
    items_count = main_page.get_items_count()
    main_page.add_all_item_to_cart()
    main_page.open_cart()
    cart_page.should_be_all_added_items(items_count)

def test_deletion_all_from_cart(main_page, cart_page, login_page):
    login_page.standard_login()
    main_page.add_all_item_to_cart()
    main_page.open_cart()
    cart_items = len(cart_page.get_added_items())
    cart_page.delete_all_from_cart()
    cart_page.should_be_empty_cart(cart_items)

# def test_fill_checkout_information(main_page, login_page, cart_page, ):
#     pass

