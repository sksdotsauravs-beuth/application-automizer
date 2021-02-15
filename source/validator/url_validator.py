import validators


class UrlValidator:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-06
        - changed:            2021-02-07

        This class will validate passed url.
    """

    # public

    def __init__(self, url: str):
        self.__url = url

    def is_valid(self) -> bool:
        """
            This method will check if the passed url is valid.
        """

        return self.__is_valid_url()

    # private

    def __is_valid_url(self) -> bool:
        return validators.url(self.__url)
