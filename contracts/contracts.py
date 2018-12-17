"""
Contracts are agreements between a function and its users. They ensure
that the data flow is consistent and correct among components.

Input and output contracts ensure that the data piped in and out
respectively are well-formed.
"""
import inspect

from functools import wraps
from contracts.exceptions import InputContractException, OutputContractException


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