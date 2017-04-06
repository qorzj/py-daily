from datetime import datetime, timedelta
import re

def calc_date_delta(query):
    """
    >>> calc_date_delta('1 days after 2017-04-30')
    '2017-05-01'
    >>> calc_date_delta('2 days before 2017/5/1')
    '2017-04-29'
    >>> calc_date_delta('10000 days after 1993/3/6')
    '2020-07-22'
    """
    segs = query.lower().split()
    assert len(segs) == 4
    assert segs[1] in ('day', 'days')
    assert segs[2] in ('after', 'before')
    delta_days = int(segs[0])
    delta_direct = 1 if segs[2] == 'after' else -1
    dates = {}
    assert dates.setdefault('dates', re.search(r'(\d{4})\D(\d{1,2})\D(\d{1,2})', segs[3]))
    origin_date = datetime.strptime('-'.join(dates['dates'].groups()), '%Y-%m-%d')
    result_date = origin_date + timedelta(days=delta_days*delta_direct)
    return result_date.strftime('%Y-%m-%d')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
