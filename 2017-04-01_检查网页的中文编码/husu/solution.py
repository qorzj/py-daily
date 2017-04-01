import requests


def get_page_encoding(url):
    curEncode = "unknown"
    try:
        curEncode=requests.get(url).encoding
    except Exception as e:
        print(e)
    finally:
        return curEncode



xx = get_page_encoding("https://www.douban.com")
print(xx)
