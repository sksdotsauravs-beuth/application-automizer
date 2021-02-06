import os


class FileUtils:
    """
        author:             Saurav Kumar Saha
        created:            2021-02-05
        changed:            2020-02-05

        This class will provide certain file functionality, like:

            - creating a file
            - checking for existence
    """

    @staticmethod
    def exists(absolute_file_path):
        """
            This method will check whether a file exists (True) or not (False).
        """

        return os.path.isfile(absolute_file_path)
