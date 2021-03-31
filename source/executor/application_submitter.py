import sys
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.factory.configuration_factory import ConfigurationFactory
from source.factory.driver_factory import DriverFactory
from source.model.log_level import LogLevel
from source.output.logger import Logger
from source.pages.house_of_nations.english_page import EnglishPage
from source.pages.house_of_nations.home_page import HomePage
from source.pages.house_of_nations.reservation_page1 import ReservationPage1
from source.pages.house_of_nations.reservation_page2 import ReservationPage2


class ApplicationSubmitter:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-05
        - changed:            2021-02-13

        This class holds the actual program functionality.
    """

    # public

    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path
        self.__configuration = None
        self.__logger = None
        self.__driver = None

    def initialize(self):
        """
            This method will initialize the class properties.
        """

        self.__configuration = ConfigurationFactory.build(self.__yaml_file_path)
        self.__logger = Logger(self.__configuration.configuration_info.log_level)
        self.__driver = DriverFactory.get_instance(
            self.__configuration.configuration_info.driver_info
        )

    def set_dry_run_parameter_configuration(self):
        """
            This method will set the dry run parameter information inside configuration.
        """

        self.__configuration.configuration_info.dry_run = "yes"

    def go_to_home_page(self) -> HomePage:
        """
            This method will emulate a browser session to visit home page
        """

        homepage = HomePage(self.__configuration, self.__driver)
        self.__logger.print_log_message(
            LogLevel.INFO,
            '>>> Go to home page...'
        )
        self.__driver.get(homepage.get_url())
        if homepage.at():
            self.__logger.print_log_message(
                LogLevel.INFO,
                '>>> Currently at home page...'
            )
        else:
            raise RuntimeError(">>> Not at home page...")

        return homepage

    def move_to_english_page_from_home(self, homepage: HomePage):
        """
            This method will emulate a browser session moving to english page
        """

        self.__logger.print_log_message(
            LogLevel.INFO,
            '>>> Go to english version of home page...'
        )

        # move cursor to language menu
        action = ActionChains(self.__driver)
        action.move_to_element(
            homepage.get_language_menu()
        ).perform()

        # wait until english option is visible on hover
        wait = WebDriverWait(self.__driver, 5)
        wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, homepage.get_xpath_english_sub_menu())
            )
        )

        # click on the language option
        homepage.get_english_sub_menu().click()

        # wait until reservation button is clickable
        english_page = EnglishPage(self.__driver)
        wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, english_page.get_xpath_reservation_button())
            )
        )

        if english_page.at():
            self.__logger.print_log_message(
                LogLevel.INFO,
                '>>> Currently at english version of home page...'
            )
        else:
            raise RuntimeError(">>> Not at english version of home page...")

        return english_page

    def move_to_reservation_step1_from_english(self, english_page: EnglishPage):
        """
            This method will emulate a browser session moving to reservation step-1
        """

        self.__logger.print_log_message(
            LogLevel.INFO,
            '>>> Go to reservation step-1...'
        )

        # move cursor to reservation button
        action = ActionChains(self.__driver)
        action.move_to_element(
            english_page.get_reservation_button()
        ).perform()

        # click on the reservation button
        english_page.get_reservation_button().click()

        # switch to reservation page tab
        self.__driver.switch_to_window(self.__driver.window_handles[1])

        reservation_page1 = ReservationPage1(self.__configuration, self.__driver)

        # wait until next button is visible
        wait = WebDriverWait(self.__driver, 5)
        wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, reservation_page1.get_xpath_next_button())
            )
        )

        if reservation_page1.at():
            self.__logger.print_log_message(
                LogLevel.INFO,
                '>>> Currently at reservation step-1...'
            )
        else:
            raise RuntimeError(">>> Not at reservation page-1...")

        return reservation_page1

    def fill_step1_information_and_move_to_step_2(self, reservation_page1: ReservationPage1):
        self.__logger.print_log_message(
            LogLevel.INFO,
            '>>> Fill up step-1 information...'
        )

        # fill all the information
        reservation_page1.fill_start_month_tag()
        reservation_page1.fill_start_month()
        reservation_page1.fill_start_year()
        reservation_page1.fill_end_month_tag()
        reservation_page1.fill_end_month()
        reservation_page1.fill_end_year()
        reservation_page1.fill_room_choices()

        # move cursor to next button
        action = ActionChains(self.__driver)
        action.move_to_element(
            reservation_page1.get_next_button()
        ).perform()

        # submit by clicking next button
        reservation_page1.get_next_button().click()

        reservation_page2 = ReservationPage2(self.__configuration, self.__driver)

        # wait until next button is visible
        wait = WebDriverWait(self.__driver, 5)
        wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, reservation_page2.get_xpath_english_lang_label())
            )
        )

        # move cursor to english language selection label
        action = ActionChains(self.__driver)
        action.move_to_element(
            reservation_page2.get_english_language_label()
        ).perform()

        # submit by clicking english language selection label
        reservation_page2.get_english_language_label().click()

        # wait until next button is visible
        wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, reservation_page2.get_xpath_next_button())
            )
        )

        if reservation_page2.at():
            self.__logger.print_log_message(
                LogLevel.INFO,
                '>>> Currently at reservation step-2...'
            )
        else:
            raise RuntimeError(">>> Not at reservation page-2...")

        reservation_page2.find_room_selection_radio_by_criteria()

        # wait for 5 seconds
        time.sleep(5)

        return reservation_page2

    def shutdown(self):
        """
            This method will shutdown the application.
        """

        if self.__driver:
            self.__logger.print_log_message(LogLevel.INFO, '>>> Shut down application...')
            self.__quit_driver()

        sys.exit()

    def get_logger(self) -> Logger:
        """
            This method will return the logger instance
        """

        return self.__logger

    logger = property(get_logger)

    def dry_run_enabled(self) -> bool:
        """
            This method will return if dry run option is active or not
        """

        return self.__configuration.configuration_info.dry_run == "yes"

    # private

    def __quit_driver(self):
        self.__driver.quit()
