import chardet
import requests
def get_page_encoding(url):
    '''
    接插url对应编码格式
    >>> url = 'http://www.baidu.com'
    >>> solution.get_page_encoding(url)
    {'confidence': 0.99, 'encoding': 'utf-8'}
    >>>
    :param url:
    :return:
    '''
    response = requests.get(url, timeout=5)
    return chardet.detect(response.content)

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    get_page_encoding(url)