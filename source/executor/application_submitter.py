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
from source.pages.house_of_nations.home_page import HomePage


class ApplicationSubmitter:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-05
        - changed:            2021-02-07

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

        # wait for 5 seconds
        time.sleep(5)

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
