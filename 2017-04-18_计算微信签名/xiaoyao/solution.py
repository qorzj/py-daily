# -*- coding:utf-8 -*-
import hashlib
import random
import string
import time

chars = string.digits + string.ascii_letters


def get_signature(url, ticket, timestamp=None, noncestr=None):
    """
    >>> get_signature('http://mp.weixin.qq.com?params=value',\
    'sM4AOVdWfPE4DxkXGEs8VMCPGGVi4C3VM0P37wVUCFvkVAy_90u5h9nbSlYy3-Sl-HhTdfl2fzFy1AOcHKP7qg','1414587457','Wm3WZYTPz0wzccnW')
    '0f9de62fce790f9a083d5c99e95740ceb90c27ed'
    """
    user_params = dict()
    user_params["url"] = url
    user_params["jsapi_ticket"] = ticket
    user_params["timestamp"] = get_timestamp() if not timestamp else timestamp
    user_params["noncestr"] = get_noncestr() if not noncestr else noncestr
    return hashlib.sha1('&'.join(k+'='+v for k, v in sorted(user_params.items())).encode()).hexdigest()


def get_noncestr():
    return ''.join(random.choice(chars) for i in range(16))


def get_timestamp():
    return str(int(time.time()))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

