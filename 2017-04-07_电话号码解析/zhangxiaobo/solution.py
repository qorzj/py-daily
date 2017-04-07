import re


def parse_to_tuple(s):
    partten = re.compile(r'\(([\d]+)\)(\d+)@(.+)')
    if len(partten.findall(s)) == 0:
        return '正确格式为 (023)68001111@office '
    else:
        return partten.findall(s)[0]


def parse_to_dict(s):
    partten = re.compile(r'\(([\d]+)\)(\d+)@(.+)')
    info = {}
    result = partten.findall(s)
    if len(result) == 0:
        return '正确格式为 (023)68001111@office '
    else:
        info['area'] = result[0][0]
        info['tel'] = result[0][1]
        info['addr'] = result[0][2]
        return info

print(parse_to_tuple('(023)68001111@office'))
print(parse_to_dict('(023)68001111@office'))

