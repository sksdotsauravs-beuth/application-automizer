import os
from selenium import webdriver
from source.model import Configuration


class DriverFactory:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-01-16
        - changed:            2021-02-03

        This class works as a factory for creating selenium
        web driver instance. More support of drivers are
        planned to be added later.
    """

    @staticmethod
    def get_driver_instance(configuration: Configuration) -> webdriver:
        """
            This method will return the driver instance based on
            provided Configuration instance.
        """
        if configuration.configuration_info.get_driver_type() == "chrome":
            print("returning driver ...")
            return webdriver.Chrome(
                executable_path=os.path.join(
                    configuration.configuration_info.get_driver_path(),
                    "chromedriver"
                )
            )
