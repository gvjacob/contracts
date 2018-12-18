# Tests for contracts
import pytest

from contracts import ic, oc, InputContractException, OutputContractException
from qualifiers import natural, positive_integer


@ic(val = natural)
def ic_echo(val):
    return val

def test_correct_ic_echo():
    assert ic_echo(3) == 3

def test_violating_ic_echo():
    with pytest.raises(InputContractException) as e:
        ic_echo(-1)


@oc(natural)
def oc_echo(val):
    return val

def test_correct_oc_echo():
    assert oc_echo(3) == 3

def test_violating_oc_echo():
    with pytest.raises(OutputContractException) as e:
        oc_echo(-1)
        

@oc(positive_integer)
@ic(val = natural)
def oc_ic_echo(val):
    return val

def test_correct_oc_ic_echo():
    assert oc_ic_echo(3) == 3

def test_violating_oc_ic_echo():
    with pytest.raises(OutputContractException) as e:
        oc_ic_echo(0)