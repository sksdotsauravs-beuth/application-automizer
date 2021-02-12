from source.model.log_level import LogLevel
import logging


class Logger:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-07

        This class will log certain messages based on the given log level.
    """

    def __init__(self, log_level: LogLevel):
        self.__log_level = log_level

    def print_log_message(self, log_level: LogLevel, message: str):
        """
            This method will print the passed message if the application
            LogLevel is greater than the passed LogLevel.
        """

        if self.__log_level.value >= log_level.value:
            logging.info(message)
            #print(message.encode('cp1252', errors='ignore'))
