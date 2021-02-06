import os
from selenium import webdriver
from source.model import DriverInfo


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
    def get_driver_instance(driver_info: DriverInfo) -> webdriver:
        """
            This method will return the driver instance based on
            provided DriverInfo instance.
        """
        if driver_info.get_driver_type() == "chrome":
            return webdriver.Chrome(
                executable_path=os.path.join(
                    driver_info.get_driver_path(),
                    "chromedriver"
                )
            )
        else:
            raise NotImplemented(f"No support yet for browser_type: {driver_info.get_driver_type()}")
