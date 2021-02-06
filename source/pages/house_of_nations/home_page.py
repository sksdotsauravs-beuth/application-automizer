class HomePage:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2021-02-05

        This class holds the information of home page, such as:
        it's url and other page elements.
    """

    __url = "https://www.house-of-nations.de/"

    def get_url(self):
        """
        :return: This method returns the home page url
        """
        return type(self).__url

    url = property(get_url)
