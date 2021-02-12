import unittest

import bs4
import os
import selenium

from source.infrastructure.requirements_reader import RequirementsReader


class InfrastructureTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-12-17
        - changed:            2021-02-07

        This class performs unit tests for the version of used libraries
        in requirements.txt file.
    """

    __reader = RequirementsReader(
        os.path.join(os.getcwd(), 'requirements.txt')
    )

    def test_beautifulsoup4(self):
        version = bs4.__version__
        self.assertEqual(self.__reader.get_version_of('beautifulsoup4'), version)

    def test_selenium(self):
        version = selenium.__version__
        self.assertEqual(self.__reader.get_version_of(selenium.__name__), version)


if __name__ == '__main__':
    unittest.main()
