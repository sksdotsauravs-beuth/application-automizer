class Logger:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-06
        changed:            2021-02-06

        This class will log certain messages based on the given log level.
    """

    def __init__(self, log_level):
        self.__log_level = log_level

    def print_log_message(self, message, log_level):
        if self.__log_level.value >= log_level.value:
            print(message)
