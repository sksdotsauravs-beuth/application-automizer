import os
import unittest

import bs4
import selenium
import validators
import yaml

from source.infrastructure.requirements_reader import RequirementsReader


class LibraryVersionTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-12-17
        - changed:            2021-02-07

        This class performs tests to check if the required version of used
        libraries matches from requirements.txt file.
    """

    def setUp(self):
        self.__reader = RequirementsReader(
            os.path.join(os.getcwd(), 'requirements.txt')
        )

    def test_beautifulsoup4(self):
        version = bs4.__version__
        self.assertEqual(self.__reader.get_version_of('beautifulsoup4'), version)

    def test_selenium(self):
        version = selenium.__version__
        self.assertEqual(self.__reader.get_version_of('selenium'), version)

    def test_pyyaml(self):
        version = yaml.__version__
        self.assertEqual(self.__reader.get_version_of('pyyaml'), version)

    def test_validators(self):
        version = validators.__version__
        self.assertEqual(self.__reader.get_version_of('validators'), version)


if __name__ == '__main__':
    unittest.main()
