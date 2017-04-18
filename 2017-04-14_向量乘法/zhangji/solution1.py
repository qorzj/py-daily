from collections import Iterable


class Vector(list):
    """
    >>> Vector(1, 2, 3) * Vector(1, 2, 3)
    Vector(1, 4, 9)
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
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            super().__init__(args[0])
        else:
            super().__init__(args)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(x * other for x in self)
        elif len(self) != len(other):
            raise ValueError("can't multiply vectors with different length")
        else:
            return Vector(x * y for x, y in zip(self, other))

    def __repr__(self):
        return 'Vector({})'.format(super().__repr__()[1:-1])

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
