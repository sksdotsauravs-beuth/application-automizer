from datetime import datetime
from source.model.driver_info import DriverInfo
from source.model.configuration_info import ConfigurationInfo
from source.model.log_level import LogLevel
from source.model.reservation_step1_info import ReservationStep1Info
from source.utils.file_utils import FileUtils
from source.validator.url_validator import UrlValidator


class Configuration:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-07

        This class represents a configuration .yml file.
    """

    # public

    def __init__(self, configuration_info: ConfigurationInfo):
        """
            This constructor will set all needed attributes.
        """

        self.__configuration_info = ConfigurationInfo()
        self.__validate(configuration_info)

    def get_configuration_info(self) -> ConfigurationInfo:
        return self.__configuration_info

    configuration_info = property(get_configuration_info)

    # private

    def __validate(self, configuration_info: ConfigurationInfo):
        self.__init_log_level(configuration_info.log_level)
        self.__init_dry_run(configuration_info.dry_run)
        self.__init_driver_info(configuration_info)
        self.__init_hon_home_url(configuration_info.hon_home_url)
        self.__init_reservation_step1_info(configuration_info)

    def __init_log_level(self, log_level: LogLevel):
        """
            This method will validate and set the log level.
        """

        if (
                log_level == LogLevel.ERROR or
                log_level == LogLevel.DEBUG or
                log_level == LogLevel.INFO
        ):
            self.__configuration_info.log_level = log_level
        else:
            raise ValueError("invalid value for log level...")

    def __init_dry_run(self, dry_run: str):
        """
            This method will validate and set the dry run value.
        """

        if dry_run == "yes" or dry_run == "no":
            self.__configuration_info.dry_run = dry_run
        else:
            raise ValueError("invalid value for dry run...")

    def __init_driver_info(self, configuration_info: ConfigurationInfo):
        """
            This method will validate and set the driver_info object.
        """

        if FileUtils.is_dir(configuration_info.driver_path):
            self.__configuration_info.driver_path = configuration_info.driver_path
        else:
            raise ValueError("invalid value for driver_path...")

        if configuration_info.driver_type == "chrome":
            self.__configuration_info.driver_type = configuration_info.driver_type
        else:
            raise ValueError(
                f"No support yet for browser_type: {configuration_info.driver_type}"
            )

        self.__configuration_info.driver_info = DriverInfo(
            self.__configuration_info.driver_path,
            self.__configuration_info.driver_type
        )

    def __init_hon_home_url(self, hon_home_url: str):
        """
            This method will validate and set the hon_home_url value.
        """

        if UrlValidator(hon_home_url):
            self.__configuration_info.hon_home_url = hon_home_url
        else:
            raise ValueError("invalid value for hon_home_url...")

    def __init_reservation_step1_info(self, configuration_info: ConfigurationInfo):
        """
            This method will validate and set the reservation_step1_info object.
        """

        self.__validate_month_tag(
            month_tag=configuration_info.start_month_tag,
            period="start"
        )
        self.__validate_month_year(
            param=configuration_info.start_month,
            period="start",
            validator=Configuration.__month_validator
        )
        self.__validate_month_year(
            param=configuration_info.start_year,
            period="start",
            validator=Configuration.__year_validator
        )

        self.__validate_month_tag(
            month_tag=configuration_info.end_month_tag,
            period="end"
        )
        self.__validate_month_year(
            param=configuration_info.end_month,
            period="end",
            validator=Configuration.__month_validator
        )
        self.__validate_month_year(
            param=configuration_info.end_year,
            period="end",
            validator=Configuration.__year_validator
        )

        self.__validate_room_choices(
            room_choices=configuration_info.room_choices
        )

        self.__configuration_info.reservation_step1_info = \
            ReservationStep1Info(
                start_month_tag=self.__configuration_info.start_month_tag,
                start_month=self.__configuration_info.start_month,
                start_year=self.__configuration_info.start_year,
                end_month_tag=self.__configuration_info.end_month_tag,
                end_month=self.__configuration_info.end_month,
                end_year=self.__configuration_info.end_year,
                room_choices=Configuration.__csv_to_list(
                    self.__configuration_info.room_choices
                )
            )

    def __validate_month_tag(self, month_tag: str, period: str):
        valid_month_tags = ["Beginning of", "Middle of", "End of"]
        is_valid_month_tag = False
        if period == "start" and month_tag in valid_month_tags[0:2]:
            is_valid_month_tag = True
            self.__configuration_info.start_month_tag = month_tag
        elif period == "end" and month_tag in valid_month_tags[1:3]:
            is_valid_month_tag = True
            self.__configuration_info.end_month_tag = month_tag

        if not is_valid_month_tag:
            raise ValueError(f"invalid value for {period}_month_tag...")

    def __validate_month_year(self, param: str, period: str, validator):
        param_type = "month" if validator.__name__.startswith("__month") else "year"
        if validator(param):
            if period == "start" and param_type == "month":
                self.__configuration_info.start_month = param
            elif period == "end" and param_type == "month":
                self.__configuration_info.end_month = param
            elif period == "start" and param_type == "year":
                self.__configuration_info.start_year = param
            elif period == "end" and param_type == "year":
                self.__configuration_info.end_year = param
        else:
            raise ValueError(f"invalid value for {period}_{param_type}...")

    def __validate_room_choices(self, room_choices: str):
        room_choices_list = Configuration.__csv_to_list(room_choices)
        if Configuration.__room_choice_validator(room_choices_list):
            self.__configuration_info.room_choices = room_choices
        else:
            raise ValueError("invalid value for room_choices...")

    @staticmethod
    def __month_validator(month: str) -> bool:
        valid_months = [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"
        ]
        return month in valid_months

    @staticmethod
    def __year_validator(year: str) -> bool:
        current_year = datetime.now().year
        return current_year <= int(year) <= (current_year + 5)

    @staticmethod
    def __room_choice_validator(room_choices: list) -> bool:
        valid_room_choices = ["EZ", "EA", "EA2", "DA", "DAB"]
        for choice in room_choices:
            if choice not in valid_room_choices:
                return False
        return True

    @staticmethod
    def __csv_to_list(csv_param: str) -> list:
        return [item.strip() for item in csv_param.split(",")]
