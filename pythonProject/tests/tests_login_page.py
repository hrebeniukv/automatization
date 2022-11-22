import pytest
from time import sleep
from utilities.config_parser import ReadConfig


def test_redirection_to_create_account(open_login_page):
    login_page = open_login_page
    register_page = login_page.click_create_account_button()
    assert register_page.is_visible_submit_button() is True, 'You are not redirected to the register page'


def test_redirection_to_reset_password(open_login_page):
    login_page = open_login_page
    reset_password_page = login_page.click_reset_password_button()
    assert reset_password_page.is_visible_reset_my_password_button() is True, \
        'You are not redirected to the reset password page'


def test_protected_password_field(open_login_page):
    login_page = open_login_page
    fild_data = login_page.set_password(ReadConfig.get_password()).get_data_password_field()
    assert fild_data is True, 'The password field has text format'


def test_show_password(open_login_page):
    login_page = open_login_page
    fild_data = login_page.set_password(ReadConfig.get_password()).show_password().get_data_password_field()
    assert fild_data is False, 'Password is not visible after checking checkbox'


# def test_login(open_login_page):
#     login_page = open_login_page
#     dashboard_page = login_page.login(ReadConfig.get_email(), ReadConfig.get_password())
#     print(type(dashboard_page))
#     assert dashboard_page.is_visible_customer_information() is True, 'Login is unsuccessful'
def test_login1(login):
    dashboard_page = login
    assert dashboard_page.is_visible_customer_information() is True, 'Login is unsuccessful'
