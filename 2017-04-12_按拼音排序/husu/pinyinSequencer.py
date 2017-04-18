# 通过汉字获得其首字母
def get_first_pinyin(word):
    str1 = word.encode("gbk")
    w = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'w', 'x', 'y', 'z']
    char_lower = [b"\xb0\xa1", b"\xb0\xc4", b"\xb2\xc0", b"\xb4\xed", b"\xb6\xe9", b"\xb7\xa1", b"\xb8\xc0",
                  b"\xb9\xfd", b"\xbb\xf6", b"\xbf\xa5",
                  b"\xc0\xab", b"\xc2\xe7", b"\xc4\xc2", b"\xc5\xb5", b"\xc5\xbd", b"\xc6\xd9", b"\xc8\xba",
                  b"\xc8\xf5", b"\xcb\xf9", b"\xcd\xd9", b"\xce\xf3", b"\xd1\x88", b"\xd4\xd0", b"\xd7\xf9"]
    cls = [x for x in char_lower if str1 >= x]
    return w[len(cls)]


print(get_first_pinyin('找'))
