import yaml
from source.model.configuration import Configuration
from source.model.configuration_info import ConfigurationInfo
from source.model.log_level import LogLevel


class ConfigurationFactory:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-13

        This class represents a configuration .yml file. Important settings
        can be defined inside this file like:

            - log level
            - dry run flag
            - selenium driver type,
            - selenium driver path,
            - page urls

        All methods are static.
    """

    # public

    @staticmethod
    def build(path_to_yml_file: str):
        """
            This method will build an instance of 'Configuration' class
            by passing a .yml file as parameter after checking if the
            given file is a valid .yml file.
        """

        if not ConfigurationFactory.__is_valid_yml_file(path_to_yml_file):
            raise IOError("'" + str(path_to_yml_file) + "' is not a valid yml file...")
        else:
            yaml_content = ConfigurationFactory.__open_yml_file(path_to_yml_file)
            return ConfigurationFactory.__build_configuration_from_yml_file(yaml_content)

    # private

    @staticmethod
    def __is_valid_yml_file(path_to_yml_file: str) -> bool:
        """
            This method will check if the given file is a valid .yml file.
        """

        return path_to_yml_file.endswith(".yml") or path_to_yml_file.endswith(".yaml")

    @staticmethod
    def __open_yml_file(path_to_yml_file: str):
        """
            This method will open a .yml file in read mode.
        """

        yaml_content = None

        with open(path_to_yml_file, 'r', encoding='utf8') as stream:
            try:
                yaml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("could not read yml file '" + str() + "'...\n" + str(exc) + "...")

        return yaml_content

    @staticmethod
    def __build_configuration_from_yml_file(yaml_content: dict) -> Configuration:
        """
            This method will build all necessary attributes for a
            'Configuration' instance and pass it to the class
            constructor.
        """

        log_level = ConfigurationFactory.__get_log_level(yaml_content)
        dry_run = ConfigurationFactory.__get_dry_run(yaml_content)
        driver_path = ConfigurationFactory.__get_driver_path(yaml_content)
        driver_type = ConfigurationFactory.__get_driver_type(yaml_content)
        hon_home_url = ConfigurationFactory.__get_hon_home_url(yaml_content)
        start_month_tag = ConfigurationFactory.__get_step1_start_month_tag(yaml_content)
        start_month = ConfigurationFactory.__get_step1_start_month(yaml_content)
        start_year = ConfigurationFactory.__get_step1_start_year(yaml_content)
        end_month_tag = ConfigurationFactory.__get_step1_end_month_tag(yaml_content)
        end_month = ConfigurationFactory.__get_step1_end_month(yaml_content)
        end_year = ConfigurationFactory.__get_step1_end_year(yaml_content)
        room_choices = ConfigurationFactory.__get_step1_room_choices(yaml_content)

        configuration_info = ConfigurationInfo()
        configuration_info.log_level = log_level
        configuration_info.dry_run = dry_run
        configuration_info.driver_path = driver_path
        configuration_info.driver_type = driver_type
        configuration_info.hon_home_url = hon_home_url
        configuration_info.start_month_tag = start_month_tag
        configuration_info.start_month = start_month
        configuration_info.start_year = start_year
        configuration_info.end_month_tag = end_month_tag
        configuration_info.end_month = end_month
        configuration_info.end_year = end_year
        configuration_info.room_choices = room_choices

        return Configuration(configuration_info)

    @staticmethod
    def __get_log_level(yaml_content: dict) -> LogLevel:
        """
            This method will fetch the log level value from a .yml file
        """

        log_level = None

        try:
            log_level_string = yaml_content['log_level']
            log_level = ConfigurationFactory.__get_log_level_value(log_level_string)
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return log_level

    @staticmethod
    def __get_log_level_value(log_level_string: str) -> LogLevel:
        log_level = None

        if log_level_string == LogLevel.ERROR.name:
            log_level = LogLevel.ERROR
        elif log_level_string == LogLevel.DEBUG.name:
            log_level = LogLevel.DEBUG
        elif log_level_string == LogLevel.INFO.name:
            log_level = LogLevel.INFO

        return log_level

    @staticmethod
    def __get_dry_run(yaml_content: dict) -> str:
        """
            This method will fetch the dry run value from a .yml file
        """

        dry_run = None

        try:
            dry_run = yaml_content['dry_run']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return dry_run

    @staticmethod
    def __get_driver_path(yaml_content: dict) -> str:
        """
            This method will fetch the driver_path value from a .yml file
        """

        driver_path = None
        try:
            driver_path = yaml_content['driver_path']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))
        return driver_path

    @staticmethod
    def __get_driver_type(yaml_content: dict) -> str:
        """
            This method will fetch the driver_type value from a .yml file
        """

        driver_type = None
        try:
            driver_type = yaml_content['driver_type']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))
        return driver_type

    @staticmethod
    def __get_hon_home_url(yaml_content: dict) -> str:
        """
            This method will fetch the hon_home_url value from a .yml file
        """

        hon_home_url = None

        try:
            hon_home_url = yaml_content['hon_home_url']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return hon_home_url

    @staticmethod
    def __get_step1_start_month_tag(yaml_content: dict) -> str:
        """
            This method will fetch the step1.start_month_tag
            value from a .yml file
        """

        start_month_tag = None

        try:
            start_month_tag = yaml_content['step1.start_month_tag']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return start_month_tag

    @staticmethod
    def __get_step1_start_month(yaml_content: dict) -> str:
        """
            This method will fetch the step1.start_month
            value from a .yml file
        """

        start_month = None

        try:
            start_month = yaml_content['step1.start_month']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return start_month

    @staticmethod
    def __get_step1_start_year(yaml_content: dict) -> str:
        """
            This method will fetch the step1.start_year
            value from a .yml file
        """

        start_year = None

        try:
            start_year = yaml_content['step1.start_year']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return start_year

    @staticmethod
    def __get_step1_end_month_tag(yaml_content: dict) -> str:
        """
            This method will fetch the step1.end_month_tag
            value from a .yml file
        """

        end_month_tag = None

        try:
            end_month_tag = yaml_content['step1.end_month_tag']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return end_month_tag

    @staticmethod
    def __get_step1_end_month(yaml_content: dict) -> str:
        """
            This method will fetch the step1.end_month
            value from a .yml file
        """

        end_month = None

        try:
            end_month = yaml_content['step1.end_month']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return end_month

    @staticmethod
    def __get_step1_end_year(yaml_content: dict) -> str:
        """
            This method will fetch the step1.end_year
            value from a .yml file
        """

        end_year = None

        try:
            end_year = yaml_content['step1.end_year']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return end_year

    @staticmethod
    def __get_step1_room_choices(yaml_content: dict) -> str:
        """
            This method will fetch the step1.room_choices
            value from a .yml file
        """

        room_choices = None

        try:
            room_choices = yaml_content['step1.room_choices']
        except KeyError as exc:
            print(ConfigurationFactory.__get_key_missing_error_message(exc))

        return room_choices

    @staticmethod
    def __get_key_missing_error_message(exc: KeyError) -> str:
        return "key does not exist in yml file: " + str(exc) + "\n"
