# from page_object.dashboard_page import DashboardPage
from utilities.web_ui.base_page import BasePage

if __name__ == "ChangePersonalDataPage":
    from page_object.dashboard_page import DashboardPage
    class ChangePersonalDataPage(BasePage):
        def __init__(self, driver):
            super().__init__(driver)

        def test(self):
            return DashboardPage(self.driver)