#!/usr/bin/python3.5
#-*- coding:utf-8 -*-
import requests
from lxml import etree
def book_info(url):
    response = requests.get(url)
    html = etree.HTML(response.text)
    segs = html.xpath('//span')
    return segs

if __name__ == '__main__':
    url = 'https://book.douban.com/subject/3227098/'
    print(book_info(url))