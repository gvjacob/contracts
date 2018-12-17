import inspect
from functools import wraps

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



def input_contract(**checks):
    """
    Input contract decorator.

    :param checks: dict, string param name to argument checker (any) -> bool
    :return: func, decorator function
    """

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            func_params = inspect.getargspec(func).args
            params_args = dict(zip(func_params, args))
            params_args.update(kwargs)
            error_params_args = {}

            for key, check in checks.items():
                try:
                    if not check(params_args[key]):
                        error_params_args[key] = params_args[key]
                except:
                    error_params_args[key] = params_args[key]
            
            if len(error_params_args) is not 0:
                raise InputContractException(error_params_args)

            result = func(*args, **kwargs)
            return result

        return decorated
    return decorator



def output_contract(check):
    """
    Output contract decorator.

    :param check: (any) -> bool, output checker
    :return: func, decorator function
    """

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if not check(result):
                raise OutputContractException(result)
            return result

        return decorated
    return decorator