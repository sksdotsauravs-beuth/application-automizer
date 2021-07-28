from selenium.webdriver.remote import webelement

from source.pages.page import Page
from source.model.configuration import Configuration
from selenium import webdriver


class HomePage(Page):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2021-07-28

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
        self.__set_attributes()

    # public

    def get_url(self) -> str:
        """
            This method returns the page url
        """

        return self.__configuration.configuration_info.hon_home_url

    def at(self) -> bool:
        """
            This method verifies if the browser is currently at page location
        """

        return self.__driver.title == self.__page_title

    def get_deny_all_cookies_except_essential_button(self) -> webelement:
        """
            This method returns the deny all but essential cookies button
        """

        return self.__driver.find_element_by_xpath(
            self.__xpath_deny_all_cookies_except_essential_button
        )

    def get_language_menu(self) -> webelement:
        """
            This method returns the language menu list item element
        """

        menu_options = self \
            .__get_nav_menu() \
            .find_element_by_tag_name("ul") \
            .find_elements_by_xpath(".//*")

        language_option = None
        for option in menu_options:
            if language_option:
                break
            css_classes = option.get_attribute("class")
            for css_class in css_classes.split():
                if 'language' in css_class:
                    language_option = option
                    break
        return language_option

    def get_english_sub_menu(self) -> webelement:
        """
            This method returns the english sub menu anchor element
        """

        return self.__driver.find_element_by_xpath(
            self.xpath_english_sub_menu
        )

    def get_xpath_english_sub_menu(self) -> str:
        """
            This method returns the english sub menu xpath
        """

        return self.__xpath_english_sub_menu

    url = property(get_url)
    xpath_english_sub_menu = property(get_xpath_english_sub_menu)

    # private

    def __set_attributes(self):
        self.__page_title = "Studentenapartments Berlin, günstige Zimmer Studenten Azubis Berlin, Zimmer mieten"
        self.__xpath_nav_menu = "/html/body/div[1]/div/header/div/div/div/div/div/nav[1]"
        self.__xpath_english_sub_menu = "//*[@id='nav-menu-item-wpml-ls-63-en']/a"
        self.__xpath_deny_all_cookies_except_essential_button = "\
        //*[@id='BorlabsCookieBox']/div/div/div/div[1]/div/div/div[2]/p[3]/a\
        "

    def __get_nav_menu(self) -> webelement:
        return self.__driver.find_element_by_xpath(
            self.__xpath_nav_menu
        )

