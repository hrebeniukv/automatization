import pytest

from page_object.login_page import LoginPage
from page_object.register_page import RegisterPage
from utilities.config_parser import ReadConfig
from utilities.driver_fectory import DriverFactory



# @pytest.fixture(scope='session')
# @pytest.fixture()
# @pytest.fixture(scope='session')
@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_browser_id())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def open_login_page(create_driver):
    create_driver.get(ReadConfig.get_login_page_url())
    return LoginPage(create_driver)

@pytest.fixture()
def open_register_page(create_driver):
    create_driver.get(ReadConfig.get_register_page_url())
    return RegisterPage(create_driver)

@pytest.fixture()
def login(open_login_page):
    return open_login_page.login(ReadConfig.get_email(), ReadConfig.get_password())


# @pytest.fixture()
# def login_into_account()