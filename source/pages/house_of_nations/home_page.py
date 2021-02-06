from source.model import Configuration


class HomePage:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2021-02-06

        This class holds the information of home page, such as:
        it's url and other page elements.
    """

    def __init__(self, configuration: Configuration):
        """
            This constructor will set all needed attributes.
        """

        self.__configuration = configuration

    def get_url(self):
        """
            This method returns the home page url
        """
        return self.__configuration.configuration_info.hon_home_url

    url = property(get_url)
