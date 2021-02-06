import yaml
from source.model.configuration import Configuration
from source.model.configuration_info import ConfigurationInfo
from source.model.log_level import LogLevel


class ConfigurationFactory:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-06

        This class represents a configuration .yml file. Important settings
        can be defined inside this file like:

            - log level
            - dry run flag
            - selenium driver type,
            - selenium driver path,
            - page urls
            - page elements xpath
            - form values

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
    def __is_valid_yml_file(path_to_yml_file):
        """
            This method will check if the given file is a valid .yml file.
        """

        return path_to_yml_file.endswith(".yml") or path_to_yml_file.endswith(".yaml")

    @staticmethod
    def __open_yml_file(path_to_yml_file):
        """
            This method will open a .yml file in read mode.
        """

        yaml_content = None

        with open(path_to_yml_file, 'r') as stream:
            try:
                yaml_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("could not read yml file '" + str() + "'...\n" + str(exc) + "...")

        return yaml_content

    @staticmethod
    def __build_configuration_from_yml_file(yaml_content):
        """
            This method will build all necessary attributes for a
            'Configuration' instance and pass it to the class
            constructor.
        """

        log_level = ConfigurationFactory.__get_log_level_from_yml_file(yaml_content)
        dry_run = ConfigurationFactory.__get_dry_run_from_yml_file(yaml_content)

        configuration_info = ConfigurationInfo()
        configuration_info.log_level = log_level
        configuration_info.dry_run = dry_run

        return Configuration(configuration_info)

    @staticmethod
    def __get_log_level_from_yml_file(yaml_content):
        """
            This method will fetch the log level value from a .yml file
        """

        log_level = None

        try:
            log_level_string = yaml_content['log_level']
            log_level = ConfigurationFactory.__get_log_level_value(log_level_string)
        except KeyError as exc:
            print("key does not exist in yml file: " + str(exc) + "\n")

        return log_level

    @staticmethod
    def __get_log_level_value(log_level_string):
        log_level = None

        if log_level_string == LogLevel.ERROR.name:
            log_level = LogLevel.ERROR
        elif log_level_string == LogLevel.DEBUG.name:
            log_level = LogLevel.DEBUG
        elif log_level_string == LogLevel.INFO.name:
            log_level = LogLevel.INFO

        return log_level

    @staticmethod
    def __get_dry_run_from_yml_file(yaml_content):
        """
            This method will fetch the dry run value from a .yml file
        """

        dry_run = None

        try:
            dry_run = yaml_content['dry_run']
        except KeyError as exc:
            print("key does not exist in yml file: " + str(exc) + "\n")

        return dry_run
