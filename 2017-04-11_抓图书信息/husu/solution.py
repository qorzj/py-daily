# coding=utf-8
import requests


def book_info(url):
    txt = requests.get(url).text
    key1 = '<meta name="keywords" content="'
    idx = txt.find(key1) + len(key1)
    tmp = txt[idx::]
    bookInf = tmp[0:tmp.find('">')].split(',')
    return {'name': bookInf[0], 'author': bookInf[1], 'press': bookInf[2]}


print(book_info("https://book.douban.com/subject/3227098/"))
