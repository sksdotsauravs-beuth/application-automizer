from factory.driver_factory import DriverFactory
from model.driver_info import DriverInfo


def print_app_name():
    print('application-automizer')


if __name__ == "__main__":
    print_app_name()

    driver_info = DriverInfo(
        driver_path="C:/Users/saurav/Downloads"
    )
    driver = DriverFactory.get_driver_instance(
        driver_info=driver_info
    )

    driver.get("https://www.house-of-nations.de/")
    print(driver.title)

    driver.close()
