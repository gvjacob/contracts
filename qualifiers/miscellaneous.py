# Miscellaneous qualifiers and convenient functions

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