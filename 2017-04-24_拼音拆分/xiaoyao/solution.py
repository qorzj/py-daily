#!/usr/bin/python3.5
import re

Shengmu = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "l", "n", "g", "k", "h", "j", "q", "x", "z",
           "c", "s", "y", "w"]

Yunmu = ['ong', 'ing', 'eng', 'ang', 'un', 'in', 'en', 'an', 'er', 've', 'ue', 'ie', 'iu', 'ou', 'ao', 'ui', 'ei', 'ai'
    , 'v', 'u', 'i', 'e', 'o', 'a']

sheng = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
         'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
         'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
         'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
         'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
         'ǖ': 'v', 'ǘ': 'v', 'ǚ': 'v', 'ǜ': 'v'}


def splitPinYin(str):
    '''
    >>> splitPinYin("shí nián shēngsǐ liǎng mángmáng")
    ['shí', 'nián', 'shēng', 'sǐ', 'liǎng', 'máng']
    '''
    tmp = ''.join(list(map(lambda x: sheng[x] if x in sheng else x, str)))
    for x in Yunmu:
        tmp = tmp.replace(x, '*' * len(x))

    p = '|'.join(Shengmu)
    indexs = [m.start() for m in re.finditer(p, tmp)]
    result = []
    i = 0
    while i < len(indexs) - 1:
        result.append(str[indexs[i]:indexs[i + 1]].strip())
        i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

