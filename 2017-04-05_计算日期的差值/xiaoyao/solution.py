#!/usr/bin/python3.5
from datetime import datetime, timedelta, tzinfo
ZERO_TIME_DELTA = timedelta(0)
LOCAL_TIME_DELTA = timedelta(hours=8)


class UTC(tzinfo):
    def utcoffset(self, dt):
        return ZERO_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA


class LocalTimeZone(tzinfo):
    def utcoffset(self, dt):
        return LOCAL_TIME_DELTA

    def dst(self, dt):
        return ZERO_TIME_DELTA

    def tzname(self, dt):
        return '+08:00'


def date_distance(date_str):
    now_date = datetime.now(LocalTimeZone())
    fmt = '%Y-%m-%d'
    post_date = datetime.strptime(date_str, fmt)
    post_date = post_date.replace(tzinfo=UTC())
    return (post_date - now_date).days

if __name__ == '__main__':
    print(date_distance('2017-05-01'))

