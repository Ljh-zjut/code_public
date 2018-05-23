#-*- coding: utf-8 -*-
import urllib.error
import urllib.request
import re

pageIndex = 1
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
url = 'https://www.qiushibaike.com/text/page/' + str(pageIndex)
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    pageCode = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, pageCode)
    for item in items:
        print(item[0], item[1], item[2])

except urllib.error.URLError as e:
    if hasattr(e, "reason"):
        print(e.reason)
