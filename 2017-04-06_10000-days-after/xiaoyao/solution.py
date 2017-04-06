#!/usr/bin/python3.5
#-*- coding:utf-8 -*-
from datetime import datetime, timedelta, tzinfo, timezone
import re
def calc_date_delta(str):
    """
        >>> calc_date_delta('1 days after 2017-04-30')
        '2017-05-01'
        >>> calc_date_delta('2 days before 2017/5/1')
        '2017-04-29'
        >>> calc_date_delta('10000 days after 1993/3/6')
        '2020-07-22'
    """
    fmt = '%Y-%m-%d'
    tz = timezone(timedelta(hours=8))
    segs = str.lower().split(' ')
    delta_direct = 1 if segs[2] == 'after' else -1
    delta_days = int(segs[0])
    origin_date = [int(i) for i in re.search(r'(\d{4})\D(\d{1,2})\D(\d{1,2})', segs[3]).groups()]
    origin_date = datetime.now(tz).replace(year=origin_date[0], month=origin_date[1], day=origin_date[2]) \
                  + timedelta(days=delta_direct*delta_days)
    return origin_date.strftime(fmt)

if __name__ == '__main__':
    import doctest
    doctest.testmod()