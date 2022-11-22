import configparser
from random import randint

config = configparser.RawConfigParser()
config.read('/home/aqa/PycharmProjects/pythonProject/configurations/configuration.ini')


class ReadConfig:


    # @staticmethod
    # def get_base_url():
    #     return config.get('app_info', 'base_url')
    @staticmethod
    def get_login_page_url():
        base_url = config.get('app_info', 'base_url')
        login_endpoint = config.get('app_info', 'login_page_endpoint')
        return f'{base_url}{login_endpoint}'

    @staticmethod
    def get_register_page_url():
        base_url = config.get('app_info', 'base_url')
        register_page_endpoint = config.get('app_info', 'register_page_endpoint')
        return f'{base_url}{register_page_endpoint}'

    @staticmethod
    def get_email():
        return config.get('user_data', 'email')

    @staticmethod
    def get_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')

    # @staticmethod
    # def get_login_page_endpoint():
    #     return config.get('browser_data', 'login_page_endpoint')
    #
    # @staticmethod
    # def get_register_page_endpoint():
    #     return config.get('browser_data', 'register_page_endpoint')

    @staticmethod
    def get_name_registration():
        return config.get('user_data_registration', 'name')

    @staticmethod
    def get_last_name_registration():
        return config.get('user_data_registration', 'last_name')

    @staticmethod
    def get_email_registration():
        domain = config.get('user_data_registration', 'domain')
        return f'{ReadConfig.get_name_registration()}+{randint(0, 1000)}{domain}'




