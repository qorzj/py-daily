"""我就想试试写一下循环啥的"""


def reverse_sentence(s):
    result = ""
    for word in s.split():
        result = result + (word[::-1]) + " "
    return result[0:-1]


print(reverse_sentence("xdsf dsfdf sdfds"))
