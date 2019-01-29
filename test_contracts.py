# Tests for contracts
import pytest
import inspect

from contracts import ic, oc, InputContractException, OutputContractException
from contracts import natural, compose, positive, positive_integer

@ic(val=natural)
def ic_echo(val):
    """ic echo"""
    return val


def test_correct_ic_echo():
    assert ic_echo(3) == 3


def test_violating_ic_echo():
    with pytest.raises(InputContractException) as e:
        ic_echo(-1)

def test_ic_echo_wraps_decorated_func():
    func_params = list(inspect.signature(ic_echo).parameters)
    assert func_params == ['val']
    assert ic_echo.__name__ == "ic_echo"
    assert ic_echo.__doc__ == "ic echo"


@oc(natural)
def oc_echo(val):
    """oc echo"""
    return val


def test_correct_oc_echo():
    assert oc_echo(3) == 3


def test_violating_oc_echo():
    with pytest.raises(OutputContractException) as e:
        oc_echo(-1)


def test_oc_echo_wraps_decorated_func():
    func_params = list(inspect.signature(oc_echo).parameters)
    assert func_params == ['val']
    assert oc_echo.__name__ == "oc_echo"
    assert oc_echo.__doc__ == "oc echo"


@oc(positive_integer)
@ic(val=natural)
def oc_ic_echo(val):
    return val


def test_correct_oc_ic_echo():
    assert oc_ic_echo(3) == 3


def test_violating_oc_ic_echo():
    with pytest.raises(OutputContractException) as e:
        oc_ic_echo(0)


@ic(val=natural)
@oc(positive_integer)
def ic_oc_echo(val):
    return val


def test_correct_ic_oc_echo():
    assert ic_oc_echo(3) == 3


def test_violating_ic_oc_echo():
    with pytest.raises(InputContractException) as e:
        ic_oc_echo(0)


@ic(val=compose(natural, positive))
def composed_ic_echo(val):
    return val


def test_correct_composed_ic_echo():
    assert composed_ic_echo(3) == 3


def test_incorrect_composed_ic_echo():
    with pytest.raises(InputContractException) as e:
        composed_ic_echo(0)

    with pytest.raises(InputContractException) as e:
        composed_ic_echo(0.2)      

    with pytest.raises(InputContractException) as e:
        composed_ic_echo(-1)


@oc(compose(natural, positive))
def composed_oc_echo(val):
    return val

def test_correct_composed_oc_echo():
    assert composed_oc_echo(3) == 3

def test_incorrect_composed_oc_echo():
    with pytest.raises(OutputContractException) as e:
        composed_oc_echo(0)

    with pytest.raises(OutputContractException) as e:
        composed_oc_echo(0.2)      

    with pytest.raises(OutputContractException) as e:
        composed_oc_echo(-1)


@ic(val1=natural, val2=positive_integer)
def ic_echo_two_vals(val1, val2):
    return (val1, val2)


def test_correct_ic_echo_two_vals():
    assert ic_echo_two_vals(0, 2) == (0, 2)

def test_incorrect_ic_echo_two_vals():
    with pytest.raises(InputContractException) as e:
        ic_echo_two_vals(0.2, -1)

    with pytest.raises(InputContractException) as e:
        ic_echo_two_vals(0, -1)

    with pytest.raises(InputContractException) as e:
        ic_echo_two_vals(-1, 2)


