Help on module solution:

NAME
    solution

FUNCTIONS
    date_distance(date_str) -> int
        求date_str和当前日期相差的天数（北京时间）
        >>> assert datetime.now().strftime('%Y-%m-%d') == '2017-04-05'
        >>> date_distance('2017-05-01')
        26
