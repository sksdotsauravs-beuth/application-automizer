import os
import unittest

from source.utils.file_utils import FileUtils


class FileUtilsTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-02-16
        - changed:            2021-02-16

        This class performs unit tests for the public methods
        in the @FileUtils class
    """

    def setUp(self) -> None:
        self.__file_path = os.path.abspath(__file__)

    def test_exists(self):
        self.assertTrue(FileUtils.exists(self.__file_path))

    def test_exists_with_non_existing_file(self):
        self.assertFalse(FileUtils.exists('C:\\invalid_file.xyz'))

    def test_is_dir(self):
        self.assertTrue(FileUtils.is_dir(os.path.dirname(self.__file_path)))

    def test_is_dir_when_dir_does_not_exist(self):
        self.assertFalse(FileUtils.is_dir(self.__file_path))


if __name__ == '__main__':
    unittest.main()
