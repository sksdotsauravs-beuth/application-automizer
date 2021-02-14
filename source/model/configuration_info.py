from source.model.log_level import LogLevel
from source.model.driver_info import DriverInfo
from source.model.reservation_step1_info import ReservationStep1Info


class ConfigurationInfo:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-13

        This class represents a data holder for configuration
        information which comes from a .yaml file.
    """

    def __init__(self):
        self.__log_level = None
        self.__dry_run = None
        self.__driver_type = None
        self.__driver_path = None
        self.__driver_info = None
        self.__hon_home_url = None
        self.__start_month_tag = None
        self.__start_month = None
        self.__start_year = None
        self.__end_month_tag = None
        self.__end_month = None
        self.__end_year = None
        self.__room_choices = None
        self.__reservation_step1_info = None

    def get_log_level(self) -> LogLevel:
        """
            This method will return log level for the application.
        """

        return self.__log_level

    def set_log_level(self, log_level: LogLevel):
        """
            This method will set the log level for this application.
        """

        self.__log_level = log_level

    def get_dry_run(self) -> str:
        """
            This method will return the dry run value.
        """

        return self.__dry_run

    def set_dry_run(self, dry_run: str):
        """
            This method will set the dry run value.
        """

        self.__dry_run = dry_run

    def get_driver_path(self) -> str:
        """
            This method will return the driver_path value.
        """

        return self.__driver_path

    def set_driver_path(self, driver_path: str):
        """
            This method will set the driver_path value.
        """
        self.__driver_path = driver_path

    def get_driver_type(self) -> str:
        """
            This method will return the driver_type value.
        """

        return self.__driver_type

    def set_driver_type(self, driver_type: str):
        """
            This method will set the driver_type value.
        """

        self.__driver_type = driver_type

    def get_driver_info(self) -> DriverInfo:
        """
            This method will return the driver_info object.
        """

        return self.__driver_info

    def set_driver_info(self, driver_info: DriverInfo):
        """
            This method will set the driver_info object.
        """

        self.__driver_info = driver_info

    def get_hon_home_url(self) -> str:
        """
            This method will return the hon_home_url value.
        """

        return self.__hon_home_url

    def set_hon_home_url(self, hon_home_url: str):
        """
            This method will set the hon_home_url value.
        """

        self.__hon_home_url = hon_home_url

    def get_start_month_tag(self) -> str:
        """
            This method will return the start_month_tag value.
        """

        return self.__start_month_tag

    def set_start_month_tag(self, start_month_tag: str):
        """
            This method will set the start_month_tag value.
        """
        self.__start_month_tag = start_month_tag

    def get_start_month(self) -> str:
        """
            This method will return the start_month value.
        """

        return self.__start_month

    def set_start_month(self, start_month: str):
        """
            This method will set the start_month value.
        """
        self.__start_month = start_month

    def get_start_year(self) -> str:
        """
            This method will return the start_year value.
        """

        return self.__start_year

    def set_start_year(self, start_year: str):
        """
            This method will set the start_year value.
        """
        self.__start_year = start_year

    def get_end_month_tag(self) -> str:
        """
            This method will return the end_month_tag value.
        """

        return self.__end_month_tag

    def set_end_month_tag(self, end_month_tag: str):
        """
            This method will set the end_month_tag value.
        """
        self.__end_month_tag = end_month_tag

    def get_end_month(self) -> str:
        """
            This method will return the end_month value.
        """

        return self.__end_month

    def set_end_month(self, end_month: str):
        """
            This method will set the end_month value.
        """
        self.__end_month = end_month

    def get_end_year(self) -> str:
        """
            This method will return the end_year value.
        """

        return self.__end_year

    def set_end_year(self, end_year: str):
        """
            This method will set the end_year value.
        """
        self.__end_year = end_year

    def get_room_choices(self) -> str:
        """
            This method will return the room_choices value.
        """

        return self.__room_choices

    def set_room_choices(self, room_choices: str):
        """
            This method will set the room_choices value.
        """
        self.__room_choices = room_choices

    def get_reservation_step1_info(self) -> ReservationStep1Info:
        """
            This method will return the reservation_step1_info value.
        """

        return self.__reservation_step1_info

    def set_reservation_step1_info(self, reservation_step1_info: ReservationStep1Info):
        """
            This method will set the reservation_step1_info value.
        """
        self.__reservation_step1_info = reservation_step1_info

    log_level = property(get_log_level, set_log_level)
    dry_run = property(get_dry_run, set_dry_run)
    driver_path = property(get_driver_path, set_driver_path)
    driver_type = property(get_driver_type, set_driver_type)
    driver_info = property(get_driver_info, set_driver_info)
    hon_home_url = property(get_hon_home_url, set_hon_home_url)
    start_month_tag = property(get_start_month_tag, set_start_month_tag)
    start_month = property(get_start_month, set_start_month)
    start_year = property(get_start_year, set_start_year)
    end_month_tag = property(get_end_month_tag, set_end_month_tag)
    end_month = property(get_end_month, set_end_month)
    end_year = property(get_end_year, set_end_year)
    room_choices = property(get_room_choices, set_room_choices)
    reservation_step1_info = property(get_reservation_step1_info, set_reservation_step1_info)
