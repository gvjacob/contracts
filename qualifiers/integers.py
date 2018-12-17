# Qualifiers for integers
from qualifiers.miscellaneous import positive, negative

def natural(v):
    """ Is arg a natural number? """
    return integer(v) and v >= 0

def integer(v):
    """ Is arg an integer? """
    return type(v) is int

def positive_integer(v):
    """ Is arg a positive integer? """
    return integer(v) and positive(v)

def negative_integer(v):
    """ Is arg a negative integer? """
    return integer(v) and negative(v)