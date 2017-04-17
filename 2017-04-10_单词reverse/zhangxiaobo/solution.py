def my_reverse(s):
    """
    >>> my_reverse("this is daily test")
    'siht si yliad tset'
    """
    lst = list(s)
    lst.reverse()
    new_lst = ''.join(lst).split()
    return ' '.join(new_lst[::-1])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
