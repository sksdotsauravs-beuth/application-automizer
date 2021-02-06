from source.model.configuration_info import ConfigurationInfo
from source.model.log_level import LogLevel


class Configuration:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-06
        changed:            2021-02-06

        This class represents a configuration .yml file.
    """

    # public

    def __init__(self, configuration_info: ConfigurationInfo):
        """
            This constructor will set all needed attributes.
        """

        self.__configuration_info = ConfigurationInfo()
        self.__validate_configuration_info(configuration_info)

    def get_configuration_info(self):
        return self.__configuration_info

    configuration_info = property(get_configuration_info)

    # private

    def __validate_configuration_info(self, configuration_info):
        self.__init_log_level(configuration_info)
        self.__init_dry_run(configuration_info.dry_run)

    def __init_log_level(self, configuration_info):
        """
            This method will validate and set the log level.
        """

        if (
            configuration_info.log_level == LogLevel.ERROR or
            configuration_info.log_level == LogLevel.DEBUG or
            configuration_info.log_level == LogLevel.INFO
        ):
            self.__configuration_info.log_level = configuration_info.log_level
        else:
            raise ValueError("invalid value for log level...")

    def __init_dry_run(self, dry_run):
        """
            This method will validate and set the dry run value.
        """

        if dry_run == "yes" or dry_run == "no":
            self.__configuration_info.dry_run = dry_run
        else:
            raise ValueError("invalid value for dry run...")