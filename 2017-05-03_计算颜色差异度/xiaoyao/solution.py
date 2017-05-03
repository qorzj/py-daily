#!/usr/bin/python3.5
from functools import reduce


def segment(s):
    s = s[1:]
    index = 0
    while index < len(s) - 1:
        yield s[index:index + 2]
        index += 2


def color_diff(c1, c2):
    """
    >>> color_diff('#000000', '#FFFFFF')
    765
    >>> color_diff('#FF0000', '#FFFFFF')
    510
    """
    return reduce(int.__add__, map(lambda x: abs(HextoInt(x[0]) - HextoInt(x[1])), zip(segment(c1), segment(c2))))


def HextoInt(s):
    return int(s, 16)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
