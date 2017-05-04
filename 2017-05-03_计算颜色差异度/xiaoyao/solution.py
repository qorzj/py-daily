#!/usr/bin/python3.5


def segment(s):
    for index in range(1, len(s), 2):
        yield int((s[index:index + 2]), 16)


def color_diff(c1, c2):
    """
    >>> color_diff('#000000', '#FFFFFF')
    765
    >>> color_diff('#FF0000', '#FFFFFF')
    510
    """
    return sum(abs(x - y) for x, y in zip(segment(c1), segment(c2)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
