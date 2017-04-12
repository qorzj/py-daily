"""我就想试试写一下循环啥的"""


def reverse_sentence(s):
    result = []
    for word in s.split():
        result.append(word[::-1])
    return ' '.join(result)


print(reverse_sentence("xdsf dsfdf sdfds"))