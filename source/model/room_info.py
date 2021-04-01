import re


class RoomInfo:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-04-01
        - changed:            2021-04-01

        This class holds the information of room entry:
            - house_name: house name of the room
            - room_type: type of room
            - number_of_persons: number of persons for
            - free_at: available from date
            - price_euro: monthly price in euro
            - size_square_meter: size in square meter
            - floor: floor of the room
            - radio_id: unique radio id of the room
    """

    # public

    def __init__(self,
                 house_name: str,
                 room_type: str,
                 number_of_persons: str,
                 free_at: str,
                 price_euro: str,
                 size_square_meter: str,
                 floor: str,
                 radio_id: str):
        """
            This constructor will set the class instance attributes.
        """

        self.__house_name = house_name
        self.__room_type = room_type
        self.__number_of_persons = number_of_persons
        self.__free_at = free_at
        self.__price_euro = price_euro
        self.__size_square_meter = size_square_meter
        self.__floor = floor
        self.__radio_id = radio_id

    def get_house_name(self) -> str:
        """
            This method will return house_name.
        """

        return self.__house_name

    def get_room_type(self) -> str:
        """
            This method will return room_type
        """

        return self.__room_type

    def get_number_of_persons(self) -> str:
        """
            This method will return number_of_persons
        """

        return self.__number_of_persons

    def get_free_at(self) -> str:
        """
            This method will return free_at
        """

        return self.__free_at

    def get_price_euro(self) -> str:
        """
            This method will return price_euro
        """

        return self.__price_euro

    def get_size_square_meter(self) -> str:
        """
            This method will return size_square_meter
        """

        return self.__size_square_meter

    def get_floor(self) -> str:
        """
            This method will return floor
        """

        return self.__floor

    def get_radio_id(self) -> str:
        """
            This method will return radio_id
        """

        return self.__radio_id

    def get_details(self) -> str:
        """
            This method will return details of a room entry
        """

        return f'{self.__house_name}|' \
               f'{self.__room_type}|' \
               f'{self.__number_of_persons}|' \
               f'{self.__free_at}|' \
               f'{self.__price_euro}|' \
               f'{self.__size_square_meter}|' \
               f'{self.__floor}|' \
               f'{self.__radio_id}'

    def get_price(self) -> float:
        """
            This will return the price in float
        """

        return float(
            re.findall(r'\d+\.\d+', self.__price_euro)[0]
        )

    house_name = property(get_house_name)
    room_type = property(get_room_type)
    number_of_persons = property(get_number_of_persons)
    free_at = property(get_free_at)
    price_euro = property(get_price_euro)
    size_square_meter = property(get_size_square_meter)
    floor = property(get_floor)
    radio_id = property(get_radio_id)
