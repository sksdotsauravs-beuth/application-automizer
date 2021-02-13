from app_info import AppInfo
from source.executor.application_submitter import ApplicationSubmitter
from source.model.log_level import LogLevel

import traceback


class AppExecutor:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2020-02-07

        This class will execute the ApplicationSubmitter class by providing specific output.
        In addition to that it will execute pre and post actions.
    """

    def __init__(self, parameter_validator):
        self.__parameter_validator = parameter_validator
        self.__logger = None

    # public

    def run(self):
        """
            This method will run the actual application.
        """
        if self.__parameter_validator.is_dry_run_call():
            self.__run_dry()
        if self.__parameter_validator.is_normal_run_call():
            self.__run_normal()
        if self.__parameter_validator.is_help_call():
            self.__display_help()
        if self.__parameter_validator.is_version_call():
            print(AppInfo.get_version())

    # private

    def __run_dry(self):
        application = self.__create_application()
        application.set_dry_run_parameter_configuration()
        self.__run(application)

    def __run_normal(self):
        application = self.__create_application()
        self.__run(application)

    def __create_application(self):
        submitter = ApplicationSubmitter(
            str(self.__parameter_validator.get_argv()[1])
        )
        submitter.initialize()
        self.__logger = submitter.logger
        return submitter

    # noinspection PyBroadException
    def __run(self, application):
        try:
            self.__display_begin_message()
            self.__handle_pre_steps()

            if application.dry_run_enabled():
                self.__logger.print_log_message(
                    LogLevel.INFO,
                    '>>> Executing dry-run...'
                )

            home = application.go_to_home_page()
            english = application.move_to_english_page_from_home(home)
            application.move_to_reservation_page_1_from_english(english)

            self.__handle_post_steps()
        except Exception:
            self.__logger.print_log_message(
                LogLevel.ERROR,
                traceback.print_exc()
            )
        finally:
            application.shutdown()

    def __display_begin_message(self):
        self.__logger.print_log_message(LogLevel.INFO, self.__get_artwork())
        processing_string = ">>> Process '" + str(self.__parameter_validator.get_argv()[1]) + "'..."
        self.__logger.print_log_message(LogLevel.INFO, processing_string)

    def __handle_pre_steps(self):
        self.__logger.print_log_message(LogLevel.INFO, ">>> Execute preparation actions...")

    def __handle_post_steps(self):
        self.__logger.print_log_message(LogLevel.INFO, ">>> Execute post actions...")

    def __display_help(self):
        print(self.__get_artwork())
        print(self.__get_help_message())

    @staticmethod
    def __get_help_message() -> str:
        star_line = 68 * "*"
        hyphen_line = 68 * "-"
        dot_line = 68 * "."
        spaces_help_line = 32 * " "
        newline = "\n"

        def __n_tab(n: int) -> str:
            return n * "\t"
        normal_run_command = "python app.py config.yml"
        dry_run_command = "python app.py config.yml --dry-run"
        version_command = "python app.py --version"
        message = \
            star_line + newline + \
            spaces_help_line + "Help" + spaces_help_line + newline + \
            star_line + newline + \
            newline + \
            "Command" + __n_tab(5) + "Description" + newline + \
            hyphen_line + newline + \
            normal_run_command + __n_tab(2) + "runs the application" + newline + \
            dot_line + newline + \
            dry_run_command + __n_tab(1) + "runs the application except" + newline + \
            __n_tab(5) + "submitting final form" + newline + \
            dot_line + newline + \
            version_command + __n_tab(3) + "prints out the current" + newline +\
            __n_tab(5) + "application version" + newline + \
            dot_line + newline

        return message

    @staticmethod
    def __get_artwork() -> str:
        return AppInfo.get_text_logo() + " v" + AppInfo.get_version() + "\n"

