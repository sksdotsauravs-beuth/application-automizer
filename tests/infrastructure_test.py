import unittest

import bs4
import os
import selenium

from source.infrastructure import RequirementsReader


class InfrastructureTest(unittest.TestCase):

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
