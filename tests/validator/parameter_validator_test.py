import os
import unittest

from source.validator.parameter_validator import ParameterValidator


class ParameterValidatorTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-02-16
        - changed:            2021-02-16

        This class performs unit tests for the public methods
        in the @ParameterValidator class
    """

    def setUp(self) -> None:
        self.__app_param = "app.py"
        self.__version_param = "--version"
        self.__help_param = "--help"
        self.__config_file_param = os.path.abspath(
            os.path.join("resource", "config.yml")
        )
        self.__dry_run_param = "--dry-run"

    def test_get_argv(self):
        expected_argv = list()
        expected_argv.append(self.__app_param)
        expected_argv.append(self.__config_file_param)
        self.assertEqual(
            expected_argv,
            ParameterValidator(
                [self.__app_param, self.__config_file_param]
            ).get_argv()
        )

    def test_is_help_call(self):
        argv = [self.__app_param, self.__help_param]
        self.assertTrue(ParameterValidator(argv).is_help_call())

    def test_is_version_call(self):
        argv = [self.__app_param, self.__version_param]
        self.assertTrue(ParameterValidator(argv).is_version_call())

    def test_is_normal_run_call(self):
        argv = [self.__app_param, self.__config_file_param]
        self.assertTrue(ParameterValidator(argv).is_normal_run_call())

    def test_is_dry_run_call(self):
        argv = [self.__app_param, self.__config_file_param, self.__dry_run_param]
        self.assertTrue(ParameterValidator(argv).is_dry_run_call())

    def test_is_valid(self):
        argv = [self.__app_param, self.__config_file_param]
        self.assertTrue(ParameterValidator(argv).is_valid())

    def test_is_valid_with_invalid__argv(self):
        argv = [self.__config_file_param]
        self.assertFalse(ParameterValidator(argv).is_valid())


if __name__ == '__main__':
    unittest.main()
