from source.model import LogLevel, DriverInfo


class ConfigurationInfo:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-07

        This class represents a data holder for configuration
        information which comes from a .yaml file.
    """

    def __init__(self):
        self.__log_level = None
        self.__dry_run = None
        self.__driver_type = None
        self.__driver_path = None
        self.__driver_info = None
        self.__hon_home_url = None
        self.__hon_home_title = None

    def get_log_level(self) -> LogLevel:
        """
            This method will return log level for the application.
        """

        return self.__log_level

    def set_log_level(self, log_level: LogLevel):
        """
            This method will set the log level for this application.
        """

        self.__log_level = log_level

    def get_dry_run(self) -> str:
        """
            This method will return the dry run value.
        """

        return self.__dry_run

    def set_dry_run(self, dry_run: str):
        """
            This method will set the dry run value.
        """

        self.__dry_run = dry_run

    def get_driver_path(self) -> str:
        """
            This method will return the driver_path value.
        """

        return self.__driver_path

    def set_driver_path(self, driver_path: str):
        """
            This method will set the driver_path value.
        """
        self.__driver_path = driver_path

    def get_driver_type(self) -> str:
        """
            This method will return the driver_type value.
        """

        return self.__driver_type

    def set_driver_type(self, driver_type: str):
        """
            This method will set the driver_type value.
        """

        self.__driver_type = driver_type

    def get_driver_info(self) -> DriverInfo:
        """
            This method will return the driver_info object.
        """

        return self.__driver_info

    def set_driver_info(self, driver_info: DriverInfo):
        """
            This method will set the driver_info object.
        """

        self.__driver_info = driver_info

    def get_hon_home_url(self) -> str:
        """
            This method will return the hon_home_url value.
        """

        return self.__hon_home_url

    def set_hon_home_url(self, hon_home_url: str):
        """
            This method will set the hon_home_url value.
        """

        self.__hon_home_url = hon_home_url

    def get_hon_home_title(self) -> str:
        """
            This method will return the hon_home_title value.
        """

        return self.__hon_home_title

    def set_hon_home_title(self, hon_home_title: str):
        """
            This method will set the hon_home_title value.
        """

        self.__hon_home_title = hon_home_title

    log_level = property(get_log_level, set_log_level)
    dry_run = property(get_dry_run, set_dry_run)
    driver_path = property(get_driver_path, set_driver_path)
    driver_type = property(get_driver_type, set_driver_type)
    driver_info = property(get_driver_info, set_driver_info)
    hon_home_url = property(get_hon_home_url, set_hon_home_url)
    hon_home_title = property(get_hon_home_title, set_hon_home_title)
