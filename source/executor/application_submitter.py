class ApplicationSubmitter:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-05
        changed:            2021-02-05

        This class holds the actual program functionality.
    """

    def __init__(self, yaml_file_path):
        self.__yaml_file_path = yaml_file_path

    @staticmethod
    def get_version():
        """
            This method will print out the version of this application.
        """
        return "2021.2.0"
