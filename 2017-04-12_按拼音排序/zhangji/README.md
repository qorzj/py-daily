```
Help on module solution:

NAME
    solution

FUNCTIONS
    pinyin_sort(names)
        >>> r = [('张三', 'Zhāng sān'), ('张珊', 'zhāng shān'), ('李四', 'lǐ sì')]
        >>> pinyin_sort(r)
        >>> r
        [('李四', 'lǐ sì'), ('张三', 'Zhāng sān'), ('张珊', 'zhāng shān')]
    
    trim_diacritic(s)
        >>> a = "Zhāng sān zhāng shān lǐ sì xī'ān"
        >>> trim_diacritic(a)
        'zhang san zhang shan li si xi an'
```
