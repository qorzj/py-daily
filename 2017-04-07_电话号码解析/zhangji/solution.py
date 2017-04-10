import re


def parse_to_tuple(s):
    """
    >>> s = "(023)68001111@office"
    >>> parse_to_tuple(s)
    ('023', '68001111', 'office')
    """
    return re.search(r'\((\d+)\)(\d+)@(.+)', s).groups()


def parse_to_dict(s):
    """
    >>> s = "(023)68001111@office"
    >>> parse_to_dict(s)
    {'area': '023', 'tel': '68001111', 'addr': 'office'}
    """
    return re.search(r'\((?P<area>\d+)\)(?P<tel>\d+)@(?P<addr>.+)', s).groupdict()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
