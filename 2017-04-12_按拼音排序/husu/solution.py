from pypinyin import pinyin
import pypinyin


def pinyin_sort(words):
    return sorted(words, key=lambda x: pinyin(x, style=pypinyin.NORMAL))


w = ['不', '帮', '好', '过', '熬', '爱']
print(pinyin_sort(w))
