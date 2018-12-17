# Qualifiers for numbers
from qualifiers.miscellaneous import positive, negative
from qualifiers.integers import integer

def number(v):
    """ Is arg a number? """
    return integer(v) or isinstance(v, float)

def positive_number(v):
    """ Is arg a positive number? """
    return number(v) and positive(v)

def negative_number(v):
    """ Is arg a negative number? """
    return number(v) and negative(v)
