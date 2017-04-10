#!/usr/bin/python3.5
#-*- coding:utf-8 -*-
def reverse_sentence(para):
    """
        >>> para = "abc def opqrst vw"
        >>> reverse_sentence(para)
        'cba fed tsrqpo wv'
    """
    return ' '.join(map(lambda param: param[::-1], para.split()))


def reverse_sentence2(para):
    """
        >>> para = "abc def opqrst vw"
        >>> reverse_sentence2(para)
        'cba fed tsrqpo wv'
    """
    from functools import reduce
    return reduce(lambda x, y: '%s %s' % (x, y), map(lambda param: param[::-1], para.split()))

if __name__ == '__main__':
    import doctest
    doctest.testmod()