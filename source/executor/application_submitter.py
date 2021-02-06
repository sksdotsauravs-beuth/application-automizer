from source.factory import ConfigurationFactory, DriverFactory
from source.model import LogLevel
from source.output import Logger
from source.pages.house_of_nations import HomePage


class ApplicationSubmitter:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-05
        changed:            2021-02-05

        This class holds the actual program functionality.
    """

    # public

    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path
        self.__configuration = None
        self.__logger = None
        self.__driver = None

    def create_configuration(self):
        """
            This method will create a configuration based on a specific .yml file.
        """

        self.__configuration = ConfigurationFactory.build(self.__yaml_file_path)
        self.__logger = Logger(self.__configuration.configuration_info.log_level)
        self.__driver = DriverFactory.get_driver_instance(self.__configuration)

    def get_configuration(self):
        """
            This method will return the initial configuration.
        """

        return self.__configuration

    def set_dry_run_parameter_configuration(self):
        """
            This method will set the dry run parameter information inside configuration.
        """

        self.__configuration.configuration_info.dry_run = "yes"

    def visit_home_page(self):
        homepage = HomePage(self.__configuration)
        self.logger.print_log_message(f'home_url: {homepage.url}', LogLevel.INFO)
        self.__driver.get(homepage.url)
        self.logger.print_log_message(f'home_title: {self.__driver.title}', LogLevel.INFO)

    def shutdown(self):
        self.__close_driver()

    def get_logger(self):
        return self.__logger

    def set_logger(self, logger):
        self.__logger = logger

    logger = property(get_logger, set_logger)

    # private

    def __dry_run_enabled(self):
        return self.__configuration.configuration_info.dry_run == "yes"

    def __close_driver(self):
        self.__driver.close()

    @staticmethod
    def get_version():
        """
            This method will print out the version of this application.
        """
        return "2021.2.0"
