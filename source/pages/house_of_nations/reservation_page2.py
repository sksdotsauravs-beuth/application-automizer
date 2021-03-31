from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from source.model.configuration import Configuration
from source.pages.page import Page


class ReservationPage2(Page):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-03-16
        - changed:            2021-03-31

        This class holds the information of reservation page 2, such as:
        it's url and other page elements.
    """

    def __init__(self, configuration: Configuration, driver: webdriver):
        """
            This constructor will set all needed attributes.
        """

        super().__init__()
        self.__configuration = configuration
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

        return 'step_active' in self.__get_step_2_div().get_attribute("class")

    def get_next_button(self) -> webelement:
        """
            This method returns the next button element
        """

        return self.__driver.find_element_by_xpath(
            self.xpath_next_button
        )

    def get_xpath_next_button(self) -> str:
        """
            This method returns the next button xpath
        """

        return self.__xpath_next_button

    def get_english_language_label(self) -> webelement:
        """
            This method returns the english language label element
        """

        return self.__driver.find_element_by_xpath(
            self.xpath_english_lang_label
        )

    def get_xpath_english_lang_label(self) -> str:
        """
            This method returns the english lang label xpath
        """

        return self.__xpath_english_lang_label

    def find_room_selection_radio_by_criteria(self) -> webelement:
        """
            This method returns the room selection radio element
        """

        room_listing_section = self.__get_room_listing_section()
        location_div_list = room_listing_section.find_elements(By.XPATH, ".//div[@class='room_listing_bg']")
        for location_div in location_div_list:
            print(location_div.find_element(By.XPATH, ".//div[1]/div[1]/h2[@class='room_data_headline']").text)

    url = property(get_url)
    xpath_next_button = property(get_xpath_next_button)
    xpath_english_lang_label = property(get_xpath_english_lang_label)

    # private

    def __set_attributes(self):
        self.__page_url = "https://reservation.house-of-nations.de/hon/whm_showunit.php"
        self.__xpath_step_2_div = "/html/body/header/div[2]/div[2]"
        self.__xpath_next_button = "/html/body/form/section[2]/input[2]"
        self.__xpath_english_lang_label = "/html/body/header/div[1]/form/label[2]"
        self.__xpath_room_listing_section = "//*[@id='content']"

    def __get_step_2_div(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_step_2_div
        )

    def __get_room_listing_section(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_listing_section
        )
