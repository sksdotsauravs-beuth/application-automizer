from source.pages import Page
from source.model import Configuration
from selenium import webdriver


class HomePage(Page):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2021-02-07

        This class holds the information of home page, such as:
        it's url and other page elements.
    """

    def __init__(self, configuration: Configuration, driver: webdriver):
        """
            This constructor will set all needed attributes.
        """

        super().__init__()
        self.__configuration = configuration
        self.__driver = driver

    def get_url(self) -> bool:
        """
            This method returns the home page url
        """
        return self.__configuration.configuration_info.hon_home_url

    def at(self) -> bool:
        """
            This method returns the home page url
        """
        return self.__driver.title == self.__configuration.configuration_info.hon_home_title

    url = property(get_url)
