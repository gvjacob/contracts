"""
Contracts are agreements between a function and its clients. They ensure
that the data flow is consistent and correct among components.

Input and output contracts ensure that the data piped in and out
respectively are well-formed.
"""
import inspect

from functools import wraps
from contracts.exceptions import InputContractException, OutputContractException


def zip_params_args(func, args, kwargs):
    """
    Zip the parameter names of function with its arguments. 

    :param func: (...) -> any, given function
    :param args: [any, ...], list of arguments
    :param kwargs: dict, additional key word arguments
    :return: dict, parameters to arguments
    """
    func_params = inspect.getfullargspec(func).args
    params_args = dict(zip(func_params, args))
    params_args.update(kwargs)
    return params_args


def get_violating_args(contracts, params_args):
    """
    Get all arguments that violate the contracts.

    :param contracts: dict, contracts from parameters to qualifiers
    :param params_args: dict, parameters to arguments
    :return: dict, parameters to contract violating arguments
    """
    error_params_args = {}
    for param, contract in contracts.items():
        arg = params_args[param]
        try:
            if not contract(arg):
                error_params_args[param] = arg
        except:
            error_params_args[param] = arg

    return error_params_args


def input_contract(**contracts):
    """
    Input contract decorator.

    :param contracts: dict, string param name to argument checker (any) -> bool
    :return: func, decorator function
    """

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            params_args = zip_params_args(func, args, kwargs)
            error_params_args = get_violating_args(contracts, params_args)
            
            if len(error_params_args) is not 0:
                raise InputContractException(error_params_args)

            return func(*args, **kwargs)

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