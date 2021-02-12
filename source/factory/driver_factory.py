import os
from selenium import webdriver
from source.model.driver_info import DriverInfo


class DriverFactory:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-01-16
        - changed:            2021-02-07

        This class works as a factory for creating selenium
        web driver instance. More support of drivers are
        planned to be added later.
    """

    @staticmethod
    def get_instance(driver_info: DriverInfo) -> webdriver:
        """
            This method will return the driver instance based on
            provided Configuration instance.
        """
        if driver_info.get_driver_type() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(
                executable_path=os.path.join(
                    driver_info.get_driver_path(),
                    "chromedriver"
                ),
                chrome_options=options
            )
