import pytest
from time import sleep

from utilities.config_parser import ReadConfig


def test_rigister_new_customer(open_register_page):
    register_page = open_register_page
    dashboard_page = register_page.register_new(ReadConfig.get_name_registration(),
                                                ReadConfig.get_last_name_registration(),
                                                ReadConfig.get_email_registration(), ReadConfig.get_password())
    assert dashboard_page.is_visible_customer_information() is True, "The new account haven' beem created"


def test_protected_password_field(open_register_page):
    register_page = open_register_page
    fild_data = register_page.set_password(ReadConfig.get_password()).get_data_password_field()
    assert fild_data is True, 'The password field has text format'


def test_protected_password_confirmation_field(open_register_page):
    register_page = open_register_page
    fild_data = register_page.set_password_confirmation(ReadConfig.get_password()).get_data_password_field()
    assert fild_data is True, 'The password field has text format'


def test_show_password(open_register_page):
    register_page = open_register_page
    password_field = register_page.set_password(ReadConfig.get_password()).show_password().get_data_password_field()
    assert password_field is False, 'Password is not visible after checking checkbox'


def test_visible_information_message(open_register_page):
    register_page = open_register_page
    is_message = register_page.show_info_message()
    assert is_message is True, 'The message hasn\'t appeared'
