from collections import Iterable


class Vector(Iterable):
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
            self.value = args[0]
        else:
            self.value = args
        self.counter = -1

    def __mul__(self, n):
        if isinstance(n, int):
            return Vector([i * n for i in self.value])
        elif isinstance(n, type(self)):
            return Vector([self.value[i] * n.value[i] for i in range(len(self.value))])
        else:
            raise TypeError('invalid args')

    def __repr__(self, *args, **kwargs):
        return self.__str__()

    def __str__(self):
        return "Vector(%s)" % ', '.join(map(str, self))

    def __le__(self, *args, **kwargs):
        return len(self.value)

    def __iter__(self):
        return self.read()

    def read(self):
        for v in self.value:
            yield v




if __name__ == '__main__':
    import doctest
    doctest.testmod()
