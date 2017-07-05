from collections import Iterable


class Vector(list):
    """
    >>> Vector(1,2,3) * Vector(2,3,4)
    Vector(2, 6, 12)
    >>> Vector(1,2).product([2,3])
    Vector((1, 2), (1, 3), (2, 2), (2, 3))
    >>> len(Vector(1, 2, 3))
    3
    >>> Vector(1,2,3) + 2
    Vector(3, 4, 5)
    >>> Vector(1,2,3) + Vector(1,1,1)
    Vector(2, 3, 4)
    """

    def __init__(self, *args):  # *表示不确定的参数
        if len(args) == 1 and isinstance(args[0], Iterable):
            super().__init__(args[0])
        else:
            super().__init__(args)

    # 两个向量相乘
    def __mul__(self, value):
        if isinstance(value, int):
            return Vector(value * x for x in self)
        if isinstance(value, Iterable) and len(value) == len(self):
            return Vector(value[i] * self[i] for i in range(len(self)))
        else:
            raise ValueError("Vector can't be multiplied by another who has not the same size.")

    def __repr__(self):
        return 'Vector({})'.format(super().__repr__()[1:-1])

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(other + x for x in self)
        if isinstance(other, Iterable) and len(other) == len(self):
            return Vector(other[i] + self[i] for i in range(len(self)))
        else:
            raise ValueError("Vector can't be multiplied by another who has not the same size.")

    def __len__(self):
        return sum(1 for x in self)

    # 计算笛卡尔乘积
    def product(self, value):
        return Vector((x, y) for x in self for y in value)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
