import sys
from source.executor.app_executor import AppExecutor
from source.validator.parameter_validator import ParameterValidator


def app():

    parameter_validator = ParameterValidator(sys.argv)
    app_executor = AppExecutor(parameter_validator)

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

    app_executor.run()


app()
