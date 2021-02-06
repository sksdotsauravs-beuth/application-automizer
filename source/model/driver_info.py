class DriverInfo:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-01-16
        - changed:            2021-02-03

        This class holds the information of driver:
            - driver_path: path to driver location
            - driver_type: type of the driver (chrome, mozilla etc.)
    """

    # public

    def __init__(self, driver_path: str, driver_type: str = "chrome"):
        """
            This constructor will set the class instance attributes.
        """
        self.__driver_path = driver_path
        self.__driver_type = driver_type

    def get_driver_path(self) -> str:
        """
            This method will return the driver_path.
        """
        return self.__driver_path

    def get_driver_type(self) -> str:
        """
            This method will return the driver_type.
        """
        return self.__driver_type

    driver_path = property(get_driver_path)
    driver_type = property(get_driver_type)
