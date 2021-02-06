class ConfigurationInfo:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-06
        changed:            2021-02-06

        This class represents a data holder for configuration
        information which comes from a .yaml file.
    """

    def __init__(self):
        self.__log_level = None
        self.__dry_run = None
        self.__hon_home_url = None
        self.__driver_type = None
        self.__driver_path = None

    def get_log_level(self):
        """
            This method will return log level for the application.
        """

        return self.__log_level

    def set_log_level(self, log_level):
        """
            This method will set the log level for this application.
        """

        self.__log_level = log_level

    def get_dry_run(self):
        """
            This method will return the dry run value.
        """

        return self.__dry_run

    def set_dry_run(self, dry_run):
        """
            This method will set the dry run value.
        """

        self.__dry_run = dry_run

    def get_hon_home_url(self):
        """
            This method will return the hon_home_url value.
        """

        return self.__hon_home_url

    def set_hon_home_url(self, hon_home_url):
        """
            This method will set the hon_home_url value.
        """

        self.__hon_home_url = hon_home_url

    def get_driver_path(self):
        """
            This method will return the driver_path object.
        """

        return self.__driver_path

    def set_driver_path(self, driver_path):
        """
            This method will set the driver_path value.
        """
        self.__driver_path = driver_path

    def get_driver_type(self):
        """
            This method will return the driver_type object.
        """

        return self.__driver_type

    def set_driver_type(self, driver_type):
        """
            This method will set the driver_type value.
        """

        self.__driver_type = driver_type

    log_level = property(get_log_level, set_log_level)
    dry_run = property(get_dry_run, set_dry_run)
    hon_home_url = property(get_hon_home_url, set_hon_home_url)
    driver_path = property(get_driver_path, set_driver_path)
    driver_type = property(get_driver_type, set_driver_type)
