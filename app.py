import sys
from source.executor.app_executor import AppExecutor
from source.validator.parameter_validator import ParameterValidator


def app():
    """
        - author:             Saurav Kumar Saha
        - created:            2020-12-17
        - changed:            2021-02-07

        This method is the starting point of execution for
        the application. It checks for the validity of
        command arguments, creates an instance of
        AppExecutor and invokes executor's run() function
    """

    parameter_validator = ParameterValidator(sys.argv)

    try:
        if not parameter_validator.is_valid():
            raise ValueError
    except ValueError:
        print(
            "Invalid flag usage. One of the following errors might have occurred:" +
            "\n" +
            "-> Flag not used!" +
            "\n" +
            "-> Flag does not exist!" +
            "\n" +
            "-> Invalid flag input combination!" +
            "\n" +
            "Please use --help flag to see a list of available flags."
        )
        sys.exit()

    app_executor = AppExecutor(parameter_validator)
    app_executor.run()


app()
