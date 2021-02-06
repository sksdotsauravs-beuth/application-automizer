from source.factory import ConfigurationFactory
from source.output import Logger


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

    def create_configuration(self):
        """
            This method will create a configuration based on a specific .yml file.
        """

        self.__configuration = ConfigurationFactory.build(self.__yaml_file_path)
        self.__logger = Logger(self.__configuration.configuration_info.log_level)

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

    def get_logger(self):
        return self.__logger

    def set_logger(self, logger):
        self.__logger = logger

    logger = property(get_logger, set_logger)

    # public

    def __dry_run_enabled(self):
        return self.__configuration.configuration_info.dry_run == "yes"

    @staticmethod
    def get_version():
        """
            This method will print out the version of this application.
        """
        return "2021.2.0"
