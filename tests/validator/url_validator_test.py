import unittest

from source.validator.url_validator import UrlValidator


class UrlValidatorTest(unittest.TestCase):
    """
        - author:             Saurav Kumar Saha
        - created:            2020-02-16
        - changed:            2021-02-16

        This class performs unit tests for the public methods
        in the @UrlValidator class
    """

    def test_is_valid(self):
        validator = UrlValidator("https://www.beuth-hochschule.de/")
        self.assertTrue(validator.is_valid())

    def test_is_valid_with_invalid_url(self):
        validator = UrlValidator("invalid_url")
        self.assertFalse(validator.is_valid())


if __name__ == '__main__':
    unittest.main()
