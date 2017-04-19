# -*- coding:utf-8 -*-
import hashlib
import random
import string
import time

chars = string.digits + string.ascii_letters


def get_signature(ticket, url):
    user_params = dict()
    user_params["noncestr"] = get_noncestr()
    user_params["jsapi_ticket"] = ticket
    user_params["timestamp"] = get_timestamp()
    user_params["url"] = url
    tmp = ''
    for key in sorted(user_params.keys()):
        tmp += '&' + key + '=' + user_params[key]
    return hashlib.sha1(tmp[1:].encode()).hexdigest()


def get_signature_test():
    """
    >>> get_signature_test()
    '0f9de62fce790f9a083d5c99e95740ceb90c27ed'
    """
    user_params = dict()
    user_params["noncestr"] = 'Wm3WZYTPz0wzccnW'
    user_params[
        "jsapi_ticket"] = 'sM4AOVdWfPE4DxkXGEs8VMCPGGVi4C3VM0P37wVUCFvkVAy_90u5h9nbSlYy3-Sl-HhTdfl2fzFy1AOcHKP7qg'
    user_params["timestamp"] = '1414587457'
    user_params["url"] = 'http://mp.weixin.qq.com?params=value'
    tmp = ''
    for key in sorted(user_params.keys()):
        tmp += '&' + key + '=' + user_params[key]
    return hashlib.sha1(tmp[1:].encode()).hexdigest()


def get_noncestr():
    return ''.join(random.choice(chars) for i in range(16))


def get_timestamp():
    return str(int(time.time()))


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    print(get_signature('sM4AOVdWfPE4DxkXGEs8VMCPGGVi4C3VM0P37wVUCFvkVAy_90u5h9nbSlYy3-Sl-HhTdfl2fzFy1AOcHKP7qg',
                        'http://mp.weixin.qq.com?params=value'))
