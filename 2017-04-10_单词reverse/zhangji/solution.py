def my_reverse(s):
    """
    >>> my_reverse("abc def opqrst vw")
    'cba fed tsrqpo wv'
    """
    return ' '.join(w[::-1] for w in s.split())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
