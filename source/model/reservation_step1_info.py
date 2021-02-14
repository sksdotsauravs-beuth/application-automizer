class ReservationStep1Info:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-13
        - changed:            2021-02-13

        This class holds the information of reservation step - 1:
            - start_month_tag
            - start_month
            - start_year
            - end_month_tag
            - end_month
            - end_year
            - room_choices
    """

    # public

    def __init__(
            self,
            start_month_tag: str,
            start_month: str,
            start_year: str,
            end_month_tag: str,
            end_month: str,
            end_year: str,
            room_choices: list
    ):
        """
            This constructor will set the class instance attributes.
        """

        self.__start_month_tag = start_month_tag
        self.__start_month = start_month
        self.__start_year = start_year
        self.__end_month_tag = end_month_tag
        self.__end_month = end_month
        self.__end_year = end_year
        self.__room_choices = room_choices

    def get_start_month_tag(self) -> str:
        """
            This method will return the start_month_tag.
        """

        return self.__start_month_tag

    def get_start_month(self) -> str:
        """
            This method will return the start_month.
        """

        return self.__start_month

    def get_start_year(self) -> str:
        """
            This method will return the start_year.
        """

        return self.__start_year

    def get_end_month_tag(self) -> str:
        """
            This method will return the end_month_tag.
        """

        return self.__end_month_tag

    def get_end_month(self) -> str:
        """
            This method will return the end_month.
        """

        return self.__end_month

    def get_end_year(self) -> str:
        """
            This method will return the end_year.
        """

        return self.__end_year

    def get_room_choices(self) -> list:
        """
            This method will return room choices.
        """

        return self.__room_choices

    start_month_tag = property(get_start_month_tag)
    start_month = property(get_start_month)
    start_year = property(get_start_year)
    end_month_tag = property(get_end_month_tag)
    end_month = property(get_end_month)
    end_year = property(get_end_year)
    room_choices = property(get_room_choices)
