from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


def test_open_login_page():
    chrome_driver = Chrome('chromedriver')
    chrome_driver.get('https://www.halfprice.eu/logowanie')
    chrome_driver.maximize_window()
    time.sleep(3)
    actual_title = chrome_driver.title
    assert actual_title == 'Logowanie - HalfPrice', 'You got wrong page!!!'
    chrome_driver.close()


def test_close_cookie_popup():
    chrome_driver = Chrome('chromedriver')
    chrome_driver.get('https://www.halfprice.eu/logowanie')
    chrome_driver.maximize_window()
    time.sleep(3)
    accept_cookies_btn_locator = '//div[@class = "ot-sdk-row"]//button[2]'
    accept_cookies_btn_element = chrome_driver.find_element(By.XPATH, accept_cookies_btn_locator)
    accept_cookies_btn_element.click()
    cookies_popup_locator = '//div[@class = "ot-sdk-row"]'
    cookies_popup_element = chrome_driver.find_element(By.XPATH, cookies_popup_locator)
    time.sleep(1)
    result = cookies_popup_element.is_displayed()

    assert result is False, 'Cookies are not accepted'
    chrome_driver.close()


def test_login():
    chrome_driver = Chrome('chromedriver')
    chrome_driver.get('https://www.halfprice.eu/logowanie')
    chrome_driver.maximize_window()
    time.sleep(3)

    accept_cookies_btn_locator = '//div[@class = "ot-sdk-row"]//button[2]'
    accept_cookies_btn_element = chrome_driver.find_element(By.XPATH, accept_cookies_btn_locator)
    accept_cookies_btn_element.click()

    email = 'hrebeniukv@gmail.com',
    password = 'testHillel123!'

    email_input_locator = '//div[contains(@class, "required")]//input[@type = "email"]'
    email_input_elament = chrome_driver.find_element(By.XPATH, email_input_locator)
    time.sleep(2)
    email_input_elament.send_keys(email)

    password_input_locator = '//input[@type="password"]'
    password_input_element = chrome_driver.find_element(By.XPATH, password_input_locator)
    time.sleep(2)
    password_input_element.send_keys(password)

    login_button_lokator = '//input[@value="Zaloguj się"]'
    login_button_element = chrome_driver.find_element(By.XPATH, login_button_lokator)
    login_button_element.click()
    time.sleep(3)
    my_account_icon_locator = '//li[@class="user hidden-xs"]'
    my_account_icon_element = chrome_driver.find_element(By.XPATH, my_account_icon_locator)
    is_vible_icon = my_account_icon_element.is_displayed()

    assert is_vible_icon is True, 'You are not login'
    chrome_driver.close()


