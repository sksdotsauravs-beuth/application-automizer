import os
import unittest

from source.infrastructure.requirements_reader import RequirementsReader


class RequirementsReaderTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-02-16
        - changed:            2021-02-16

        This class performs unit tests for the public methods
        in the @RequirementsReader class
    """

    def setUp(self):
        self.__reader = RequirementsReader(
            os.path.join(os.getcwd(), 'requirements.txt')
        )

    def test_get_file_path(self):
        expected_path = os.path.abspath(
            os.path.join(os.getcwd(), 'requirements.txt')
        )
        self.assertEqual(expected_path, self.__reader.get_file_path())

    def test_get_version_of(self):
        expected_version = "3.141.0"
        self.assertEqual(expected_version, self.__reader.get_version_of('selenium'))

    def test_get_version_of_for_invalid_module(self):
        expected_version = None
        self.assertEqual(
            expected_version,
            self.__reader.get_version_of('some_invalid_module')
        )


if __name__ == '__main__':
    unittest.main()
