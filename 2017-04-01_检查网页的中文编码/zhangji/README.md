```
    get_page_encoding(url)
        检查url对应的网页的中文编码
        >>> url = 'https://www.baidu.com'
        >>> get_page_encoding(url)
        'utf-8'
        >>> url = 'http://www.tju.edu.cn/'
        >>> get_page_encoding(url)
        'gbk'
        >>> url = 'http://www.google.com'
        >>> get_page_encoding(url)
        'unknown'
```
