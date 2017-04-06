import datetime
import re 
import logging
def calc_date_delta(query):
    try:
        array_query = query.split(' ')

        str_offset = array_query[0]
        str_operator = array_query[2]
        array_start =  re.split('[\-\/]',array_query[3])

        date_start = datetime.datetime.strptime(array_start[0]+'-'+array_start[1]+'-'+array_start[2], '%Y-%m-%d')

        result = ''
        if str_operator == 'after':
            result = date_start + datetime.timedelta(days=int(str_offset))
        if str_operator == 'before':
            result = date_start - datetime.timedelta(days=int(str_offset))
        if result == '' :
            return "格式错误"
            
        return  result.strftime('%Y-%m-%d')  
    except Exception as e:
        # logging.exception(e)
        return "格式错误"
if __name__ == '__main__':
    print(calc_date_delta('10000 days after 1990-01-01'))
    print(calc_date_delta('1 days before 2017/4/6'))
    print(calc_date_delta('6 days before 2017/4/6'))
    print(calc_date_delta('31 after after 2017/4/30'))
    print(calc_date_delta('30000 after after 1993/6/30'))
    print(calc_date_delta('30000 after after 1993/6/88'))
