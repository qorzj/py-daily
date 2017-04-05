from datetime import datetime, timedelta, timezone


def date_distance(date_str) -> int:
    """求date_str和当前日期相差的天数（北京时间）
    >>> assert datetime.now().strftime('%Y-%m-%d') == '2017-04-05'
    >>> date_distance('2017-05-01')
    26
    """
    fmt = '%Y-%m-%d'
    post_date = datetime.strptime(date_str, fmt)
    now_date = datetime.strptime(
        datetime.now(
            timezone(timedelta(hours=8))
        ).strftime(fmt),
        fmt
    )
    return (post_date - now_date).days


if __name__ == '__main__':
    import doctest
    doctest.testmod()

