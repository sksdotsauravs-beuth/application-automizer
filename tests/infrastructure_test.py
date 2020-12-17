import unittest
import bs4


class InfrastructureTest(unittest.TestCase):
    def test_beautifulsoup4(self):
        version = bs4.__version__
        self.assertEqual(version, '4.9.0')


if __name__ == '__main__':
    unittest.main()
