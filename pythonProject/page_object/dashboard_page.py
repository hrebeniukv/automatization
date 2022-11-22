from selenium.webdriver.common.by import By

from page_object.ChangPersonalDataPage import ChangePersonalDataPage
from utilities.web_ui.base_page import BasePage


if __name__ == "dashboard_page":

    class DashboardPage(BasePage):
        def __init__(self, driver):
            super().__init__(driver)

        __contact_data = (By.XPATH, '//div[contains(@class, "box-information")]')
        __customer_name_last_name = (By.XPATH, '//div[contains(@class, "box-information")]//p/text()[1]')
        __change_information_data_button = (By.XPATH, '//div[contains(@class, "information")]//a/span')

        def is_visible_customer_information(self):
            return self._is_visible(self.__contact_data)

        def click_change_information_button(self):
            self._click(self.__change_information_data_button)
            return ChangePersonalDataPage(self._driver)
        #
        # def get_current_name(self):
        #     return self._get_field_value(self.__customer_name_last_name, 'value')
