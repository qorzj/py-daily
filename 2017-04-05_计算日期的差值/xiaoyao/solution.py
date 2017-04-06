#!/usr/bin/python3.5
from datetime import datetime, timedelta, tzinfo, timezone


def date_distance(date_str):
    tz = timezone(timedelta(hours=8))
    now_date = datetime.now(tz)
    fmt = '%Y-%m-%d'
    post_date = datetime.strptime(date_str, fmt)
    post_date = post_date.replace(tzinfo=tz)
    a = (post_date - now_date)
    return a.days

if __name__ == '__main__':
    print(date_distance('2017-04-08'))