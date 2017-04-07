import re


def parse_to_tuple(s):
    partten = re.compile(r'\((\d+)\)(\d+)+@(.+)')
    if partten.search(s) is None:
        return '正确格式为 (023)68001111@office '
    else:
        return partten.search(s).groups()


def parse_to_dict(s):
    partten = re.compile(r'\(([\d]+)\)(\d+)@(.+)')
    result = partten.search(s)
    if result is None:
        return '正确格式为 (023)68001111@office '
    else:
        return dict(zip(('area', 'tel', 'addr'), result.groups()))

print(parse_to_tuple('(023)68001111@office'))
print(parse_to_dict('(023)68001111@office'))

