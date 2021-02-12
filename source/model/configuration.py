from source.model.driver_info import DriverInfo
from source.model.configuration_info import ConfigurationInfo
from source.model.log_level import LogLevel
from source.utils.file_utils import FileUtils
from source.validator.url_validator import UrlValidator


class Configuration:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-07

        This class represents a configuration .yml file.
    """

    # public

    def __init__(self, configuration_info: ConfigurationInfo):
        """
            This constructor will set all needed attributes.
        """

        self.__configuration_info = ConfigurationInfo()
        self.__validate(configuration_info)

    def get_configuration_info(self) -> ConfigurationInfo:
        return self.__configuration_info

    configuration_info = property(get_configuration_info)

    # private

    def __validate(self, configuration_info: ConfigurationInfo):
        self.__init_log_level(configuration_info.log_level)
        self.__init_dry_run(configuration_info.dry_run)
        self.__init_driver_info(
            configuration_info.driver_path,
            configuration_info.driver_type
        )
        self.__init_hon_home_url(configuration_info.hon_home_url)
        self.__init_hon_home_title(configuration_info.hon_home_title)

    def __init_log_level(self, log_level: LogLevel):
        """
            This method will validate and set the log level.
        """

        if (
                log_level == LogLevel.ERROR or
                log_level == LogLevel.DEBUG or
                log_level == LogLevel.INFO
        ):
            self.__configuration_info.log_level = log_level
        else:
            raise ValueError("invalid value for log level...")

    def __init_dry_run(self, dry_run: str):
        """
            This method will validate and set the dry run value.
        """

        if dry_run == "yes" or dry_run == "no":
            self.__configuration_info.dry_run = dry_run
        else:
            raise ValueError("invalid value for dry run...")

    def __init_driver_info(self, driver_path: str, driver_type: str):
        """
            This method will validate and set the driver_info object.
        """

        if FileUtils.is_dir(driver_path):
            self.__configuration_info.driver_path = driver_path
        else:
            raise ValueError("invalid value for driver path...")

        if driver_type == "chrome":
            self.__configuration_info.driver_type = driver_type
        else:
            NotImplemented(f"No support yet for browser_type: {driver_type}")

        self.__configuration_info.driver_info = DriverInfo(driver_path, driver_type)

    def __init_hon_home_url(self, hon_home_url: str):
        """
            This method will validate and set the hon_home_url value.
        """

        if UrlValidator(hon_home_url):
            self.__configuration_info.hon_home_url = hon_home_url
        else:
            raise ValueError("invalid value for hon_home_url...")

    def __init_hon_home_title(self, hon_home_title: str):
        """
            This method will validate and set the hon_home_title value.
        """

        if hon_home_title:
            self.__configuration_info.hon_home_title = hon_home_title
        else:
            raise ValueError("invalid value for hon_home_title...")
