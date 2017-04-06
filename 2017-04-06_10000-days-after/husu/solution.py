from datetime import datetime, timedelta


def calc_date_delta(query_str)->str:
    keystrs = query_str.split(" ")
    assert 4 <= len(keystrs), "查询字符串关键字长度必须大于4"
    d = int(keystrs[0])
    d = (keystrs[2] == "before")*(-1)*d + (keystrs[2] == "after")*d
    fmt =["%Y-%m-%d","%Y/%m/%d"][keystrs[3].find("-") < 0]
    fromdate = datetime.strptime(keystrs[3], fmt)
    return (fromdate + timedelta(days=d)).strftime(fmt)

print(calc_date_delta("11 days after 2011/11/22"))