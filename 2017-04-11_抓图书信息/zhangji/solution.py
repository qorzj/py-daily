import requests
import logging


def book_info(url):
    try:
        text = requests.get(url, timeout=5).text
        assert '<span property="v:itemreviewed">' in text and '<span class="pl">出版社:</span>' in text
        meta, text = text.split('<meta name="keywords" content="', 1)[-1].split('">', 1)
        book_name, text = text.split('<span property="v:itemreviewed">', 1)[-1].split('</span>', 1)
        press, text = text.split('<span class="pl">出版社:</span>', 1)[-1].split('<br', 1)
        book_name = book_name.strip()
        press = press.strip()
        author = meta.split(book_name + ',', 1)[-1].split(',' + press, 1)[0]
        return {'name': book_name, 'author': author, 'press': press}
    except Exception as e:
        logging.exception(e)
        return 'failed'


if __name__ == '__main__':
    print(book_info('https://book.douban.com/subject/3227098/'))
    # {'name': '编程珠玑', 'press': '人民邮电出版社', 'author': 'Jon Bentley'}

    print(book_info('https://book.douban.com/subject/1139336/'))
    # {'name': 'C程序设计语言', 'press': '机械工业出版社', 'author': '（美）Brian W. Kernighan,（美）Dennis M. Ritchie'}

    print(book_info('https://book.douban.com/subject/3012360/'))
    # {'name': 'C和指针', 'press': '人民邮电出版社', 'author': 'Kenneth A.Reek'}

    print(book_info('https://read.douban.com/ebook/379531/?dcs=subject-rec&dcm=douban&dct=3012360'))
    # ERROR:root:
    # Traceback (most recent call last):
    #   File "solution.py", line 7, in book_info
    #     assert '<span property="v:itemreviewed">' in text and '<span class="pl">出版社:</span>' in text
    # AssertionError
    # failed
