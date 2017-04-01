import requests


def get_page_encoding(url):
    encode = "unknown"
    try:
        encode = requests.get(url).encoding
    except Exception as e:
        print(e)
    finally:
        return encode

xx = get_page_encoding("https://www.douban.com")
print(xx)
