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

    def get_log_level(self):
        """
            This method will return log level for the application.
        """

        return self.__log_level

    def get_dry_run(self):
        """
            This method will return the dry run value.
        """

        return self.__dry_run

    def set_log_level(self, __log_level):
        """
            This method will set the log level for this application.
        """

        self.__log_level = __log_level

    def set_dry_run(self, __dry_run):
        """
            This method will set the dry run value.
        """

        self.__dry_run = __dry_run

    log_level = property(get_log_level, set_log_level)
    dry_run = property(get_dry_run, set_dry_run)