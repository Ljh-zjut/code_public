#! usr/bin/env python3
#-*- coding: utf-8 -*-
import urllib.request
import re
req = urllib.request.urlopen('http://www.imooc.com/course/list?c=python&page=1')
buf = req.read()
buf = buf.decode('utf-8') #python3需要更改一下参数格式
pic = re.findall(r'src=.+\.jpg', buf)
print(pic)
i = 0
for url in pic:
    url2 = re.sub(r'src=\"', 'https:', url)
    print(url2)
    f = open(str(i)+'.jpg', 'wb+') #以二进制格式打开一个文件用于读写,如果只用'w'18行就会出现写入问题
    req = urllib.request.urlopen(url2)
    buf = req.read()
    f.write(buf)
    i+=1
