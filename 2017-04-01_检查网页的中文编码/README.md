## 题目

实现一个函数`get_page_encoding(url:str)->'gbk|utf-8|unknown'`，作用是给一个网页的链接，返回这个网页的中文编码是utf-8还是gbk。注意有大量的中文网站没有在meta中指定charset，但我们也要能处理这类网页（假设这些网页都是gbk或utf-8编码的）。

url是以`http://`或`https://`开头的链接地址

中文编码原理提示：
```
>>> ord('秒')
31186
>>> chr(31185), chr(31186), chr(31187), chr(3118), chr(1187), chr(187), chr(87)
('科', '秒', '秓', 'మ', 'ң', '»', 'W')
>>> '秒'.encode('utf-8')
b'\xe7\xa7\x92'
>>> '秒'.encode('gbk')
b'\xc3\xeb'
>>> 
>>> len('秒')
1
>>> len('秒差距')
3
>>> len('秒差距'.encode('utf-8'))
9
>>> len('秒差距'.encode('gbk'))
6
>>> 
```
