from abc import ABC, abstractmethod


class Page(ABC):
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-07
        - changed:            2021-02-07

        This class is an abstract class for all pages
        with abstract methods like:
            - get_url()
            - at()
    """

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_url(self) -> str:
        pass

    @abstractmethod
    def at(self) -> bool:
        pass
