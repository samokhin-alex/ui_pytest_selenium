import configparser
import os
from pathlib import Path

config = configparser.RawConfigParser()

config_path = Path(__file__).parent.parent / 'support' / 'config_data.ini'
config.read(str(config_path))

class ReadConfig:
    @classmethod
    def get_url(cls):
        url = config.get('common value', 'url')
        return url

    @classmethod
    def get_inventory_url(cls):
        inventory_url = config.get('common value', 'inventory_url')
        return inventory_url

    @classmethod
    def get_cart_url(cls):
        cart_url = config.get('common value', 'cart_url')
        return cart_url

    @classmethod
    def get_standard_user_login(cls):
        standard_user_login = config.get('common value', 'standard_user_login')
        return standard_user_login

    @classmethod
    def get_standard_user_password(cls):
        standard_user_password = config.get('common value', 'standard_user_password')
        return standard_user_password

    @classmethod
    def get_valid_first_name(cls):
        valid_first_name = config.get('common value', 'valid_first_name')
        return valid_first_name

    @classmethod
    def get_valid_last_name(cls):
        valid_last_name = config.get('common value', 'valid_last_name')
        return valid_last_name

    @classmethod
    def get_valid_postel_code(cls):
        valid_postel_code = config.get('common value', 'valid_postel_code')
        return valid_postel_code