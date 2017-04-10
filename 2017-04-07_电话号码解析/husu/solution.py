import re


def parse_to_tuple(s):
    """
    >>> s = "(023)68001111@office"
    >>> parse_to_tuple(s)
    """
    return re.search(r'\((\d+)\)(\d+)@(.+)', s).groups()


def parse_to_dict(s):
    return re.search(r'\((?P<area>\d+)\)(?P<tel>\d+)@(?P<addr>.+)', s).groupdict()


print(parse_to_dict("(023)68001111@home"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()