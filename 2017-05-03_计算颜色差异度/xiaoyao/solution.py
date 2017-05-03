#!/usr/bin/python3.5
## 题目
# 实现函数 `color_diff(c1:str, c2:str) -> int`，计算c1和c2这两个RGB颜色的差距。
#
# 具体算法例如c1='#000000', c2='#FFFFFF', 那么c1其实是(0, 0, 0), 而c2其实是(127, 127, 127)，它们的颜色差异度=`abs(0-127)+abs(0-127)+abs(0-127)`=381
#
# 所以`color_diff('#000000', '#FFFFFF')`应该等于3
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
    a = zip(segment(c1), segment(c2))
    a = map(lambda x: abs(HextoInt(x[0]) - HextoInt(x[1])), a)
    return reduce(int.__add__, a)


def HextoInt(s):
    return int(s, 16)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
