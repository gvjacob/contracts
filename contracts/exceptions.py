"""
Contract exceptions are raised when either the input or output contract 
is violated by data that pipes in or out. 
"""

class InputContractException(Exception):
    """
    Exception raised when the input contract is broken.
    """

    def __init__(self, errors):
        """
        Initialize the exception.

        :param errors: dict, dictionary from param name to argument
        """
        super(InputContractException, self).__init__(self.message(errors))


    def message(self, errors):
        """
        Formalize the contract error message from the given errors.

        :param errors: dict, param name to argument
        :return: string, error message
        """
        error_message = "\nArguments that failed the contracts"
        for key, value in errors.items():
            error_message += f"\n{key}: {str(value)}"
        return error_message



class OutputContractException(Exception):
    """
    Exception raised when the output contract is broken.
    """

    def __init__(self, output):
        """
        Initialize the exception.

        :param output: any, the output of the function
        """
        super(OutputContractException, self).__init__(self.message(output))


    def message(self, output):
        """
        Formalize the contract error message from the given errors.

        :param output: any, the output of the function
        :return: string, error message
        """
        return f"The result of {str(output)} broke the output contract"

