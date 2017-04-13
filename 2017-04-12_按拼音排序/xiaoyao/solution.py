sheng = {'a': 'āáǎà', 'o': 'ōóǒò', 'e': 'ēéěè', 'i': 'īíǐì', 'u': 'ūúǔù', 'v': 'ǖǘǚǜ'}


def return_sheng(letter):
    for key in sheng.keys():
        if letter in sheng[key]:
            return key
    return letter


def trim_diacritic(s):
    """
    >>> a = "Zhāng sān zhāng shān lǐ sì xī'ān"
    >>> trim_diacritic(a)
    'zhang san zhang shan li si xi an'
    """
    s = s.replace("'", ' ').lower()
    return ''.join(list(map(return_sheng, s)))


def pinyin_sort(names):
    """
    >>> r = [('张三', 'Zhāng sān'), ('张珊', 'zhāng shān'), ('李四', 'lǐ sì')]
    >>> pinyin_sort(r)
    [('李四', 'lǐ sì'), ('张三', 'Zhāng sān'), ('张珊', 'zhāng shān')]
    """
    return sorted(names, key=lambda x: trim_diacritic(x[1]))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
