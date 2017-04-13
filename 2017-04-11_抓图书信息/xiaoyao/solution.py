#!/usr/bin/python3.5
#-*- coding:utf-8 -*-
import requests,re
from lxml import etree
def book_info(url):
    text = requests.get(url).text
    div = re.search('[\s\S]+(<div[\s\S]*?作者[\s\S]*?出版社[\s\S]*?副标题[\s\S]*?</div>)', text).group(1)
    div = re.sub('\n|,|&nbsp;', '', div)
    div = re.findall('>([\s\S]+?)<', div)
    div = list(filter(lambda x: x.strip(), div))
    div = [re.sub('\s', '', i) for i in div]
    return div

if __name__ == '__main__':
    url = 'https://book.douban.com/subject/3227098/'
    print(book_info(url))