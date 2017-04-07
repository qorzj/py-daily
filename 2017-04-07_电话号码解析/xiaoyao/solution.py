#!/usr/bin/python3.5
#-*- coding:utf-8 -*-
import re
class parse_tel:

    """
        >>> from solution import parse_tel
        >>> parse_tel.parse_to_tuple('(023)68001111@office')
        ('023', '68001111', 'office')
        >>> parse_tel.parse_to_dict('(023)68001111@office') == {'area': '023', 'tel': '68001111', 'addr': 'office'}
        True
    """

    @staticmethod
    def parse_to_tuple(s):
        return re.search(r'\((\d+)\)(\d+)+@(.+)', s).groups()

    @staticmethod
    def parse_to_dict(s):
        return re.search(r'\((?P<area>\d+)\)(?P<tel>\d+)+@(?P<addr>.+)', s).groupdict()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
