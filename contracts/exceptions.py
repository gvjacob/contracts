"""
Contract exceptions are raised when either the input or output contract 
is violated by data that pipes in or out. 
"""

class InputContractException(Exception):
    """
    Exception raised when the input contract is broken.
    """

    def __init__(self, errors, contracts):
        """
        Initialize the exception.

        :param errors: dict, dictionary from param name to argument
        :param contracts: { string: (any) -> bool, ... }, params to contracts
        """
        reasons = { param: contract.__doc__ or '' for param, contract in contracts.items() }
        super(InputContractException, self).__init__(self.message(errors, reasons))


    def message(self, errors, reasons):
        """
        Formalize the contract error message from the given errors.

        :param errors: dict, param name to argument
        :param reasons: { string: string, ... }, param to violation reason
        :return: string, error message
        """
        error_message = "\n\nContract violating arguments:"
        for param, value in errors.items():
            error_message += f"\n\n{param}: {str(value)}\n"
            error_message += reasons[param]
        return error_message



class OutputContractException(Exception):
    """
    Exception raised when the output contract is broken.
    """

    def __init__(self, output, contract):
        """
        Initialize the exception.

        :param output: any, the output of the function
        :param contract: (any) -> bool, the contract
        """
        super(OutputContractException, self).__init__(self.message(output, contract.__doc__))


    def message(self, output, reason):
        """
        Formalize the contract error message from the given errors.

        :param output: any, the output of the function
        :param reason: string, the reason for output contract violation
        :return: string, error message
        """
        return f"\n\nThe result of {str(output)} broke the output contract\n{reason or ''}"

