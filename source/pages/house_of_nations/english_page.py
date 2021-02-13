from selenium.webdriver.remote import webelement

from source.pages.page import Page
from selenium import webdriver


class EnglishPage(Page):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-13
        - changed:            2021-02-13

        This class holds the information of english home page, such as:
        it's url and other page elements.
    """

    def __init__(self, driver: webdriver):
        """
            This constructor will set all needed attributes.
        """

        super().__init__()
        self.__driver = driver
        self.__set_attributes()

    # public

    def get_url(self) -> str:
        """
            This method returns the page url
        """
        return self.__page_url

    def at(self) -> bool:
        """
            This method verifies if the browser is currently at page location
        """
        return self.__driver.title == self.__page_title

    def get_reservation_button(self) -> webelement:
        """
            This method returns the reservation button element
        """

        return self.__driver.find_element_by_xpath(
            self.xpath_reservation_button
        )

    def get_xpath_reservation_button(self) -> str:
        """
            This method returns the reservation button xpath
        """
        return self.__xpath_reservation_button

    url = property(get_url)
    xpath_reservation_button = property(get_xpath_reservation_button)

    # private

    def __set_attributes(self):
        self.__page_url = "https://www.house-of-nations.de/en/"
        self.__page_title = "Student apartments Berlin, Single apartment, Double Apartments"
        self.__xpath_reservation_button = "//*[@id='reservierung']"
