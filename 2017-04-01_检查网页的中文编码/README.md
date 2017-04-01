实现一个函数`get_page_encoding(url:str)->'gbk|utf-8|unknown'`

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
