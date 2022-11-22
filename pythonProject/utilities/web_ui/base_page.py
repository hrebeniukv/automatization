from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__waiter = WebDriverWait(driver, 8)

    def __wait_until_element_clikabl(self, locator):
        return self.__waiter.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator):
        return self.__waiter.until(EC.visibility_of_element_located(locator))

    def __wait_until_element_located(self, locator):
        return self.__waiter.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        element = self.__wait_until_element_clikabl(locator)
        element.click()

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _get_field_value(self, locator, value):
        element = self.__wait_until_element_located(locator)
        return element.get_attribute(value)

