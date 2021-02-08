import sys
from source.factory import ConfigurationFactory, DriverFactory
from source.model import LogLevel
from source.output import Logger
from source.pages.house_of_nations import HomePage


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

    def visit_home_page(self):
        """
            This method will emulate a browser session to visit home page
        """

        homepage = HomePage(self.__configuration, self.__driver)
        self.__logger.print_log_message(LogLevel.INFO, '>>> Go to home page...')
        self.__driver.get(homepage.url)
        if homepage.at():
            self.__logger.print_log_message(LogLevel.INFO, '>>> Currently at home page...')

    def shutdown(self):
        """
            This method will shutdown the application.
        """

        if self.__driver:
            self.__logger.print_log_message(LogLevel.INFO, '>>> Shut down application...')
            self.__close_driver()

        sys.exit()

    def get_logger(self) -> Logger:
        """
            This method will return the logger instance
        """

        return self.__logger

    logger = property(get_logger)

    # private

    def __dry_run_enabled(self):
        return self.__configuration.configuration_info.dry_run == "yes"

    def __close_driver(self):
        self.__driver.close()
