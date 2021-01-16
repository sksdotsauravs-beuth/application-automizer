class DriverInfo:

    def __init__(self, driver_path: str, driver_type: str = "chrome"):
        self.__driver_path = driver_path
        self.__driver_type = driver_type

    def get_driver_path(self) -> str:
        return self.__driver_path

    def get_driver_type(self) -> str:
        return self.__driver_type

    driver_path = property(get_driver_path, None)
    driver_type = property(get_driver_type, None)
