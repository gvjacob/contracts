"""
Contracts are agreements between a function and its clients. They ensure
that the data flow is consistent and correct among components.

Input and output contracts ensure that the data piped in and out
respectively are well-formed.
"""

import inspect
from functools import wraps

from contracts.exceptions import InputContractException, OutputContractException


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
                raise InputContractException(error_params_args, contracts)
            return func(*args, **kwargs)

        return decorated
    return decorator


def output_contract(contract):
    """
    Output contract decorator; check if calling 
    function with given arguments yield valid result.

    :param contract: (T) -> bool, output qualifier
    :return: decorator function
    """
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if not contract(result):
                raise OutputContractException(result, contract)
            return result

        return decorated
    return decorator


def zip_params_args(func, args, kwargs = {}):
    """
    Zip the parameter names of function with its arguments. 

    :param func: (...) -> any, given function
    :param args: [any, ...], list of arguments
    :param kwargs: { string: any, ... }, additional key word arguments
    :return: { string: any, ... }, parameters to arguments
    """
    func_params = inspect.signature(func).parameters
    params_args = dict(zip(func_params, args))
    params_args.update(kwargs)
    return params_args


def get_violating_args(contracts, params_args):
    """
    Get all arguments that violate the contracts.

    :param contracts: { string: (any) -> bool, ... }, contracts from parameters to qualifiers
    :param params_args: { string: any, ... }, parameters to arguments
    :return: { string: any, ... }, parameters to contract violating arguments
    """
    error_params_args = {}
    for param, arg in params_args.items():
        # No contract for parameter
        if param not in contracts:
            continue

        # Checking breaks
        try: 
            valid = contracts[param](arg)
        except:
            error_params_args[param] = arg
            continue

        # Violate contract
        if not valid:
            error_params_args[param] = arg
    return error_params_args