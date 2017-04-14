from collections import Iterable


class Vector(list):
    """
        >>> Vector(1, 2, 3) * Vector(2, 3, 4)
        Vector(2, 6, 12)
        >>> v = Vector(3,4,5,6)
        >>> v * 2
        Vector(6, 8, 10, 12)
        >>> v[0]
        3
        >>> v[-1]
        6
        >>> len(v)
        4
        >>> list(v)
        [3, 4, 5, 6]
        >>> str(v)
        'Vector(3, 4, 5, 6)'
        >>> sum(v)
        18
    """

    def __init__(self, *args):  # known special case of list.__init_
        if isinstance(args[0], Iterable):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)

    def __mul__(self, n):
        if isinstance(n, int):
            return Vector([i * n for i in self])
        elif isinstance(n, type(self)):
            return Vector([self[i] * n[i] for i in range(len(self))])
        else:
            raise TypeError('invalid args')

    def __repr__(self, *args, **kwargs):
        return self.__str__()

    def __str__(self):
        return "Vector(%s)" % ', '.join(map(str, self))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
