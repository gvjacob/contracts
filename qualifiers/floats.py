# Qualifiers for floats 
from qualifiers.miscellaneous import positive, negative

def floating_point(v):
    """ Is arg a floating point number ? """
    return isinstance(v, float)

def positive_float(v):
    """ Is arg a positive floating point number? """
    return floating_point(v) and positive(v)

def negative_float(v):
    """ Is arg a negative floating point number? """
    return floating_point(v) and negative(v)