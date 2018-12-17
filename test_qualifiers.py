# Tests for qualifiers
import pytest

from qualifiers import *

def suite_runner(qualifier, trues, falses):
    """
    Run func with trues and falses, checking if they yield
    True and False respectively.

    :param qualifier: (any) -> bool, qualifier
    :param trues: [any, ...], objects that should be qualified
    :param falses: [any, ...], objects that should not be qualified
    :return: bool, if all trues and falses run correctly against qualifier
    """
    all_true = all(map(qualifier, trues))
    all_false = not all(map(qualifier, falses))
    return all_true and all_false


# Miscellaneous
def test_compose():
    # test positive integer
    trues = [3, 123]
    falses = [0, -1, -5, 0.3333, -0.3333, "str", True, False, [], {}]
    composed = compose(integer, positive)
    assert suite_runner(composed, trues, falses)


def test_positive():
    trues = [3, 123, True]
    falses = [0, -1, -123, False]
    assert suite_runner(positive, trues, falses)


def test_negative():
    trues = [-1, -123]
    falses = [0, 3, 123, True]
    assert suite_runner(negative, trues, falses)


# Integers
def test_natural():
    trues = [5, 0]
    falses = [-1, 0.2, -0.3, 0.3333, -0.3333, "str", True, False, [], {}]
    assert suite_runner(natural, trues, falses)


def test_integer():
    trues = [0, 3, -1, -5]
    falses = [0.3333, -0.3333, "str", True, False, [], {}]
    assert suite_runner(integer, trues, falses)


def test_positive_integer():
    trues = [3, 123]
    falses = [0, -1, -5, 0.3333, -0.3333, "str", True, False, [], {}]
    assert suite_runner(positive_integer, trues, falses)


def test_negative_integer():
    trues = [-1, -5]
    falses = [0, 3, 123, 0.3333, -0.3333, "str", True, False, [], {}]
    assert suite_runner(negative_integer, trues, falses)
    

# Numbers
def test_number():
    trues = [0, 2, 123, 0.3333, -2, -123, -0.3333]
    falses = ["str", True, False, [], {}]
    assert suite_runner(number, trues, falses)


def test_positive_number():
    trues = [2, 123, 0.3333]
    falses = [0, -2, -123, -0.3333, "str", True, False, [], {}]
    assert suite_runner(positive_number, trues, falses)


def test_negative_number():
    trues = [-2, -123, -0.3333]
    falses = [0, 2, 123, 0.3333, "str", True, False, [], {}]
    assert suite_runner(negative_number, trues, falses)


# Floats
def test_floating_point():
    trues = [0.2, 1.333, 123.333, -0.2, -1.333, -123.333]
    falses = [0, 2, 123, -2, -123, "str", True, False, [], {}]
    assert suite_runner(floating_point, trues, falses)


def test_positive_float():
    trues = [0.2, 1.333, 123.333]
    falses = [-0.2, -1.333, -123.333, 0, 2, 123, -2, -123, "str", True, False, [], {}]
    assert suite_runner(positive_float, trues, falses)


def test_negative_float():
    trues = [-0.2, -1.333, -123.333]
    falses = [0.2, 1.333, 123.333, 0, 2, 123, -2, -123, "str", True, False, [], {}]
    assert suite_runner(negative_float, trues, falses)