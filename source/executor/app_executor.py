from app_info import AppInfo
from source.executor.application_submitter import ApplicationSubmitter
from source.model import LogLevel


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

    def __run(self, application):
        try:
            self.__display_begin_message()
            self.__handle_pre_steps()
            application.visit_home_page()
            self.__handle_post_steps()
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
        message =\
            "*******************************************************************\n" + \
            "                               Help                                \n" + \
            "*******************************************************************\n" + \
            "\n" + \
            "Command" + "\t\t\t\t\t" + "Description\n" + \
            "-------------------------------------------------------------------\n" + \
            "python app.py config.yml\t\truns the application\n" + \
            "...................................................................\n" + \
            "python app.py config.yml --dry-run\truns the application except\n" + \
            "\t\t\t\t\t" + "submitting final form\n" + \
            "...................................................................\n" + \
            "python app.py --version\t\t\tprints out the current\n" + \
            "\t\t\t\t\t" + "application version\n" + \
            "...................................................................\n"

        return message

    @staticmethod
    def __get_artwork() -> str:
        return AppInfo.get_text_logo() + " v" + AppInfo.get_version() + "\n"
