import os
from selenium import webdriver
from model.driver_info import DriverInfo


class DriverFactory:

    @staticmethod
    def get_driver_instance(driver_info: DriverInfo) -> webdriver:
        if driver_info.get_driver_type() == "chrome":
            return webdriver.Chrome(
                executable_path=os.path.join(
                    driver_info.get_driver_path(),
                    "chromedriver"
                )
            )
        else:
            raise NotImplemented(f"No support yet for browser_type: {driver_info.get_driver_type()}")
