from datetime import datetime


def date_distance(date_str):
    try:
        other_date = datetime.strptime(date_str, '%Y-%m-%d')
        now_str = datetime.now().strftime('%Y-%m-%d')
        now = datetime.strptime(now_str, '%Y-%m-%d')
        distance = (now-other_date).days
    except ValueError:
        return '{}格式错误'.format(date_str)
    if distance < 0:
        return '[ {} ]在当前时间[ {} ]后[ {} ]天'.format(date_str, datetime.now().strftime('%Y-%m-%d'), abs(distance))
    else:
        return '[ {} ]在当前时间[ {} ]前[ {} ]天'.format(date_str, datetime.now().strftime('%Y-%m-%d'), distance)

if __name__ == '__main__':
    print(date_distance('2017-03-31'))
