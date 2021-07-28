from selenium.webdriver.remote import webelement

from source.model.configuration import Configuration
from source.pages.page import Page
from selenium import webdriver
from selenium.webdriver.support.select import Select


class ReservationPage1(Page):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-13
        - changed:            2021-02-13

        This class holds the information of reservation page 1, such as:
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

        return 'step_active' in self.__get_step_1_div().get_attribute("class")

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

    def fill_start_month_tag(self):
        target = self.__configuration.configuration_info.reservation_step1_info.start_month_tag
        start_month_tag_select_element = Select(self.__get_start_month_tag_select_element())
        start_month_tag_select_element.select_by_value(target)

    def fill_start_month(self):
        target = self.__configuration.configuration_info.reservation_step1_info.start_month
        start_month_select_element = Select(self.__get_start_month_select_element())
        start_month_select_element.select_by_visible_text(target)

    def fill_start_year(self):
        target = self.__configuration.configuration_info.reservation_step1_info.start_year
        start_year_select_element = Select(self.__get_start_year_select_element())
        start_year_select_element.select_by_value(target)

    def fill_end_month_tag(self):
        target = self.__configuration.configuration_info.reservation_step1_info.end_month_tag
        end_month_tag_select_element = Select(self.__get_end_month_tag_select_element())
        end_month_tag_select_element.select_by_value(target)

    def fill_end_month(self):
        target = self.__configuration.configuration_info.reservation_step1_info.end_month
        end_month_select_element = Select(self.__get_end_month_select_element())
        end_month_select_element.select_by_visible_text(target)

    def fill_end_year(self):
        target = self.__configuration.configuration_info.reservation_step1_info.end_year
        end_year_select_element = Select(self.__get_end_year_select_element())
        end_year_select_element.select_by_value(target)

    def fill_room_choices(self):
        choices = ["EZ", "EA", "EA2", "DA", "DAB"]
        target = self.__configuration.configuration_info.reservation_step1_info.room_choices
        if choices[0] not in target:
            self.__get_room_choice_typ0_checkbox().click()
        if choices[1] not in target:
            self.__get_room_choice_typ1_checkbox().click()
        if choices[2] not in target:
            self.__get_room_choice_typ2_checkbox().click()
        if choices[3] not in target:
            self.__get_room_choice_typ3_checkbox().click()
        if choices[4] not in target:
            self.__get_room_choice_typ4_checkbox().click()

    url = property(get_url)
    xpath_next_button = property(get_xpath_next_button)

    # private

    def __set_attributes(self):
        self.__page_url = "https://reservation.house-of-nations.de/hon/index.php?lng=2"
        self.__xpath_step_1_div = "/html/body/header/div/div[3]/div[1]"
        self.__xpath_next_button = "/html/body/form/section[2]/div/div/input"
        self.__xpath_start_month_tag = "//*[@id='start_tag']"
        self.__id_start_month = "start_monat"
        self.__name_start_year = "start_jahr"
        self.__xpath_end_month_tag = "//*[@id='end_tag']"
        self.__xpath_end_month = "//*[@id='end_monat']"
        self.__xpath_end_year = "//*[@id='end_jahr']"
        self.__xpath_room_choice_typ0 = "//*[@id='typEZ']"
        self.__xpath_room_choice_typ1 = "//*[@id='typEA']"
        self.__xpath_room_choice_typ2 = "//*[@id='typEA2P']"
        self.__xpath_room_choice_typ3 = "//*[@id='typDA']"
        self.__xpath_room_choice_typ4 = "//*[@id='typDAB']"

    def __get_step_1_div(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_step_1_div
        )

    def __get_start_month_tag_select_element(self) -> webelement:
        xpath_finder = ReservationPage1.__find_element(by="xpath")
        return xpath_finder(
            driver=self.__driver,
            element_xpath=self.__xpath_start_month_tag
        )

    def __get_start_month_select_element(self) -> webelement:
        id_finder = ReservationPage1.__find_element(by="id")
        return id_finder(
            driver=self.__driver,
            element_id=self.__id_start_month
        )

    def __get_start_year_select_element(self) -> webelement:
        name_finder = ReservationPage1.__find_element(by="name")
        return name_finder(
            driver=self.__driver,
            element_name=self.__name_start_year
        )

    def __get_end_month_tag_select_element(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_end_month_tag
        )

    def __get_end_month_select_element(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_end_month
        )

    def __get_end_year_select_element(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_end_year
        )

    def __get_room_choice_typ0_checkbox(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_choice_typ0
        )

    def __get_room_choice_typ1_checkbox(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_choice_typ1
        )

    def __get_room_choice_typ2_checkbox(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_choice_typ2
        )

    def __get_room_choice_typ3_checkbox(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_choice_typ3
        )

    def __get_room_choice_typ4_checkbox(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_room_choice_typ4
        )

    @staticmethod
    def __find_element(by: str):

        def find_element_by_xpath(driver: webdriver, element_xpath: str) -> webelement:
            return driver.find_element_by_xpath(element_xpath)

        def find_element_by_id(driver: webdriver, element_id: str) -> webelement:
            return driver.find_element_by_id(element_id)

        def find_element_by_name(driver: webdriver, element_name: str) -> webelement:
            return driver.find_element_by_name(element_name)

        if by == "xpath":
            return find_element_by_xpath
        elif by == "id":
            return find_element_by_id
        elif by == "name":
            return find_element_by_name
