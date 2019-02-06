# Tests for contracts
import pytest
import inspect

from contracts import ic, oc, InputContractException, OutputContractException
from contracts import natural, compose, positive, positive_integer

class TestInputContract:

    @ic(val = positive)
    def echo_ic(self, val):
        """ echo_ic """
        return val

    @ic(missing_val = positive)
    def echo_ic_with_unmatched_keys(self, val):
        return val

    @ic()
    def echo_ic_without_keys(self, val):
        return val

    @ic(val_one = positive, val_two = natural)
    def echo_ic_two_vals(self, val_one, val_two):
        return val_one, val_two

    def test_return_val(self):
        assert self.echo_ic(1) == 1

    def test_return_val_with_unmatched_keys(self):
        assert self.echo_ic_with_unmatched_keys(1) == 1

    def test_return_val_without_keys(self):
        assert self.echo_ic_without_keys(1) == 1

    def test_violate_ic(self):
        with pytest.raises(InputContractException) as e:
            self.echo_ic(0)
    
    def test_echo_ic_two_vals_return_vals(self):
        assert self.echo_ic_two_vals(1, 2) == (1, 2)

    def test_echo_ic_two_vals_violate_ic(self):
        with pytest.raises(InputContractException) as e:
            self.echo_ic_two_vals(1, -2)

        with pytest.raises(InputContractException) as e:
            self.echo_ic_two_vals(-2, 1)

        with pytest.raises(InputContractException) as e:
            self.echo_ic_two_vals(-2, -2)

    def test_wrap_decorated_func(self):
        func_params = list(inspect.signature(self.echo_ic).parameters)
        assert func_params == ['val']
        assert self.echo_ic.__name__ == "echo_ic"
        assert self.echo_ic.__doc__ == " echo_ic "


class TestOutputContract:

    @oc(positive)
    def echo_oc(self, val):
        """ echo_oc """
        return val

    def test_return_val(self):
        assert self.echo_oc(1) == 1

    def test_violate_oc(self):
        with pytest.raises(OutputContractException) as e:
            self.echo_oc(0)

    def test_wrap_decorated_func(self):
        func_params = list(inspect.signature(self.echo_oc).parameters)
        assert func_params == ['val']
        assert self.echo_oc.__name__ == "echo_oc"
        assert self.echo_oc.__doc__ == " echo_oc "


class TestInputOutputContracts:

    @ic(val = positive)
    @oc(positive_integer)
    def echo_ic_oc(self, val):
        """ echo_ic_oc """
        return val

    def test_return_val(self):
        assert self.echo_ic_oc(1) == 1

    def test_violate_ic(self):
        with pytest.raises(InputContractException) as e:
            self.echo_ic_oc(0)
    
    def test_violate_oc(self):
        with pytest.raises(OutputContractException) as e:
            self.echo_ic_oc(1.5)

    def test_violate_ic_oc(self):
        with pytest.raises(InputContractException) as e:
            self.echo_ic_oc(0)

    def test_wrap_decorated_func(self):
        func_params = list(inspect.signature(self.echo_ic_oc).parameters)
        assert func_params == ['val']
        assert self.echo_ic_oc.__name__ == "echo_ic_oc"
        assert self.echo_ic_oc.__doc__ == " echo_ic_oc "


class TestOutputInputContracts:

    @oc(positive_integer)
    @ic(val = positive)
    def echo_oc_ic(self, val):
        """ echo_oc_ic """
        return val

    def test_return_val(self):
        assert self.echo_oc_ic(1) == 1

    def test_violate_ic(self):
        with pytest.raises(InputContractException) as e:
            self.echo_oc_ic(0)
    
    def test_violate_oc(self):
        with pytest.raises(OutputContractException) as e:
            self.echo_oc_ic(1.5)

    def test_violate_oc_ic(self):
        with pytest.raises(InputContractException) as e:
            self.echo_oc_ic(0)

    def test_wrap_decorated_func(self):
        func_params = list(inspect.signature(self.echo_oc_ic).parameters)
        assert func_params == ['val']
        assert self.echo_oc_ic.__name__ == "echo_oc_ic"
        assert self.echo_oc_ic.__doc__ == " echo_oc_ic "
