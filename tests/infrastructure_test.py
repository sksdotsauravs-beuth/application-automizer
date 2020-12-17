import unittest

import bs4
import os
import selenium

from infrastructure.requirements_processor import RequirementsProcessor


class InfrastructureTest(unittest.TestCase):

    __processor = RequirementsProcessor(os.path.join(os.getcwd(), 'requirements.txt'))
    __processor.prepare_requirements_dict()

    def test_beautifulsoup4(self):
        version = bs4.__version__
        self.assertEqual(self.__processor.get_version_of('beautifulsoup4'), version)

    def test_selenium(self):
        version = selenium.__version__
        self.assertEqual(self.__processor.get_version_of(selenium.__name__), version)


if __name__ == '__main__':
    unittest.main()
