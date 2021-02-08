class RequirementsReader:
    """
        - author:             Saurav Kumar Saha
        - created:            2020-12-17
        - changed:            2021-02-07

        This class contains information from requirements.txt file.
    """

    # public

    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__prepare_requirements_dict()

    def get_file_path(self) -> str:
        """
            This method will return the file_path.
        """
        return self.__file_path

    file_path = property(get_file_path)

    def get_version_of(self, module_name: str) -> str:
        """
            This method returns the version of given module_name.
        """
        return self.__requirements_dict.get(module_name)

    # private

    def __prepare_requirements_dict(self):
        """
            This method reads the requirements.txt file and
            prepares a dict() of versions for the packages.
        """
        self.__requirements_dict = dict()
        with open(self.__file_path) as f:
            for line in f:
                splits = line.strip().split('==')
                self.__requirements_dict[splits[0]] = splits[1]
