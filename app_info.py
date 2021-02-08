class AppInfo:
    """
        - author:             Saurav Kumar Saha
        - created:            2021-02-04
        - changed:            2021-02-07

        This class holds basic application information
    """

    @staticmethod
    def get_name() -> str:
        """
            This method will print out the name of this application.
        """

        return "Application Automizer"

    @staticmethod
    def get_version() -> str:
        """
            This method will print out the version of this application.
        """

        return "2021.2.0"

    @staticmethod
    def get_text_logo() -> str:
        """
            This method will print out the textual logo of this application.
        """

        return """
   ⢀⢀⢀⢀ ⢀⢀⢀⢀    ⢕⢕⢕⢕⢕⢕⢕⠄        
 ⢀⢕⢕⢕⢕⢕⢕⢕⠄         ⠁⠁⠕⢕⢕⢕⠅
⢀⢕⢕⠕⠁⠀⢕⢕⢕⢕         ⢄⢄⢀⢀⢐⢕⢕⠅
⢐⢕⢕⠅⠀⠀⢕⢕⢕⢕      ⢀⢐⢕⠑⠑⠕⠕⢕⢕⢕⠁
⠐⢕⢕⢕⢄⢔⢕⢕⢕⢕⢕⢕⢕ ⢐⢕⢕ ⠀⠀⠀ ⢕⢕⢕⠅
  ⠑⢕⢕⢕⢕⠕⠑⠕⠕⠕⠕⠕⠀⢐⢕⢕⢐⢕⢕⢕⢕⢕⠅
    Application Automizer
                """
