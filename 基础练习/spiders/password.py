#! usr/bin/env python3
#-*- coding:utf-8 -*-

import urllib.request
import urllib.parse

value = {"username":"827532755@qq.com","password":"ljh7010791"}
data = urllib.parse.urlencode(value).encode(encoding='UTF8') #需要转成utf-8的格式
url = "https://mail.qq.com/cgi-bin/loginpage?autologin=n&errtype=1&clientuin=827532755&param=&sp=&tfcont=22%20serialization%3A%3Aarchive%205%200%200%204%200%200%200%208%20authtype%201%204%209%20clientuin%209%20827532755%206%20domain%206%20qq.com%202%20vm%203%20wsk&r=41d8f19f55a35fe44c1c1699d3c504b0"
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
print(response.read())