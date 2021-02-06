from source.utils.file_utils import FileUtils


class ParameterValidator:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-05
        changed:            2021-02-05

        This class will validate passed parameters.
    """

    # public

    def __init__(self, argv):
        self.__argv = argv

    def is_valid(self):
        """
            This method will check if the passed parameters are valid.
        """

        return (
            self.is_version_call() or
            self.is_normal_run_call() or
            self.is_dry_run_call() or
            self.is_help_call()
        )

    def is_help_call(self):
        """
            This method will check if the help call is valid.
        """

        return self.__has_two_arguments() and str(self.__argv[1]) == "--help"

    def is_version_call(self):
        """
            This method will check if the version call is valid.
        """

        return self.__has_two_arguments() and str(self.__argv[1]) == "--version"

    def is_normal_run_call(self):
        """
            This method will check if the normal run call is valid.
        """

        return self.__has_two_arguments() and self.__parameter_file_exists()

    def is_dry_run_call(self):
        """
            This method will check if the dry run call is valid.
        """

        return len(self.__argv) == 3 and self.__parameter_file_exists() and str(self.__argv[2]) == "--dry-run"

    def get_argv(self):
        return self.__argv

    # private

    def __has_two_arguments(self):
        return len(self.__argv) == 2

    def __parameter_file_exists(self):
        return FileUtils.exists(str(self.__argv[1]))
