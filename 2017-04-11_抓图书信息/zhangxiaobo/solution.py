import re
import requests


def book_info(url):
    response = requests.get(url).text
    m = re.compile(r'[\s\S]+<meta name="keywords" content="(.*?)">[\s\S]+').search(response).groups()
    result = str(m[0]).split(',')
    return {'name': result[0], 'author': result[1], 'press': result[2]}

print(book_info('https://book.douban.com/subject/27009783/?icn=index-latestbook-subject'))
