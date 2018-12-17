# Miscellaneous
def compose(*qualifiers):
    """
    Compose given qualifiers.

    :param *qualifiers: [(any) -> bool, ...], qualifiers
    :return: (any) -> bool, composed qualifier 
    """
    def qualify(v):
        return all(map(lambda q: q(v), qualifiers))
    return qualify

def positive(v):
    return v > 0

def negative(v):
    return v < 0


# Integers
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


# Numbers
def number(v):
    """ Is arg a number? """
    return integer(v) or isinstance(v, float)

def positive_number(v):
    """ Is arg a positive number? """
    return number(v) and positive(v)

def negative_number(v):
    """ Is arg a negative number? """
    return number(v) and negative(v)


# Floats
def floating_point(v):
    """ Is arg a floating point number ? """
    return isinstance(v, float)

def positive_float(v):
    """ Is arg a positive floating point number? """
    return floating_point(v) and positive(v)

def negative_float(v):
    """ Is arg a negative floating point number? """
    return floating_point(v) and negative(v)