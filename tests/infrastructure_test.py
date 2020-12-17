import unittest
import bs4
from infrastructure.requirements_processor import RequirementsProcessor


class InfrastructureTest(unittest.TestCase):
    def test_requirements_reader(self):
        reader = RequirementsProcessor('requirements.txt')
        self.assertEqual('requirements.txt', reader.file_path)

    def test_beautifulsoup4(self):
        version = bs4.__version__
        self.assertEqual('4.9.0', version)


if __name__ == '__main__':
    unittest.main()
