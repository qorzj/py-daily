import requests
import logging
import chardet


def get_page_encoding(url):
    encode = "unknown"
    try:
        content = requests.get(url).content
        encode = chardet.detect(content)["encoding"]
    except Exception as e:
        logging.exception(e)
    finally:
        return encode


xx = get_page_encoding("http://parseccrux.qiniudn.com/4465p3cttj10.txt")
print(xx)
