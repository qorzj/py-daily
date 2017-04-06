from datetime import datetime, timedelta, timezone


def date_distance(date_str)->int:
    tz=timezone(timedelta(hours=8))
    targetDate = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=tz)
    now = datetime.now(tz)
    return (now-targetDate).days


print(date_distance("2017-04-11"))



