"""我就想试试写一下循环啥的"""


def reverse_sentence(s):
    result = ""
    for word in s.split():
        result = " ".join({result, word[::-1]})
    return result


print(reverse_sentence("xdsf dsfdf sdfds"))
