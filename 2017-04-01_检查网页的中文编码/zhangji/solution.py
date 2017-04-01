import requests
from ifsugar import _try

def get_page_encoding(url):
    """检查url对应的网页的中文编码
    >>> url = 'https://www.baidu.com'
    >>> get_page_encoding(url)
    'utf-8'
    >>> url = 'http://www.tju.edu.cn/'
    >>> get_page_encoding(url)
    'gbk'
    >>> url = 'http://www.google.com'
    >>> get_page_encoding(url)
    'unknown'
    """
    with _try:
        content = requests.get(url, timeout=5).content
        for coding in ['utf-8', 'gbk']:
            with _try:
                return [content.decode(coding)] and coding

    return 'unknown'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
