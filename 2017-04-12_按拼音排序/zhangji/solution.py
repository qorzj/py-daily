import unicodedata
import sys

_cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

def trim_diacritic(s):
    """
    >>> a = "Zhāng sān zhāng shān lǐ sì xī'ān"
    >>> trim_diacritic(a)
    'zhang san zhang shan li si xi an'
    """
    s = s.replace("'", ' ').lower()
    return unicodedata.normalize('NFD', s).translate(_cmb_chrs)


def pinyin_sort(names):
    """
    >>> r = [('张三', 'Zhāng sān'), ('张珊', 'zhāng shān'), ('李四', 'lǐ sì')]
    >>> pinyin_sort(r)
    >>> r
    [('李四', 'lǐ sì'), ('张三', 'Zhāng sān'), ('张珊', 'zhāng shān')]
    """
    names.sort(key=lambda x:trim_diacritic(x[1]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
