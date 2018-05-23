#! usr/bin/env python3
# -*- coding: utf-8 -*-
import re
strl = 'xiaomi pro 15.6'
pa = re.compile(r'xiaomi') #普通匹配
ma = pa.match(strl)
ma.span() #匹配位置
ma.group() #匹配到的字符串
ma.string #匹配到的完整字符串
pa1 = re.compile(r'xIaomI', re.I) #re.I指的是忽略大小写
ma1 = pa1.match(strl)
ma2 = re.match(r'xiaomi', strl) #match方法是将正则表达式，和需要匹配字符串写在参数中
ma3 = re.match(r'{\w}', '{x}}') #\w 任意一个单词字符
ma4 = re.match(r'{\S}', '{%}') #\d 匹配数字 \D 非数字 \s表示空白 \S表示非空白
ma5 = re.match(r'[A-Z][a-z]*', 'Aaffqqsd')
ma6 = re.match(r'[_a-zA-Z]+[_\w]*', 'htll') #+指匹配一次或多次，*表示0次或多次，？表示1次或0次
ma7 = re.match(r'[\w]{6,11}@163.com', 'ljh116547@163.com') # {m,n}匹配前一个字符m到n次，
ma8 = re.match(r'[0-9][\w]+?', '3DM')#？表示非贪婪模式
ma9 = re.match(r'[\w]{6,11}@163.com$','561369@163.com')#$表示匹配以这个字符串结尾的字符 ^表示出现在开头
ma10 = re.match(r'\Aimooc[\w]*', 'imoocpython') #\A表示指定字符串必须出现在开头 \Z表示出现在结尾
ma11 = re.match(r'[1-9]?\d$|100', '90')
ma12 = re.match(r'[\w]{6,11}@(163|126).com','561369@126.com') #可以用|来表示匹配两个字符串之一
ma13 = re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>') #\1就表示前面这个<[\w]+>
ma14 = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>') #?P<name>用于给分组起别名，?P=name用于引用这个别名的分组
se = re.search(r'\d+', 'zjut ljhmath = 90, ljhpython = 99')#search是在一个字符串中查找匹配，match是从头开始匹配
fd = re.findall(r'\d+', 'zjut ljhmath = 90, ljhpython = 99')#findall是找到匹配直接返回所有匹配部分的列表，不需要用group来显示匹配部分
sum1 = sum([int(x) for x in fd])
su = re.sub(r'\d+','100', 'zjut ljhmath = 90, ljhpython = 99') #sub将字符串中匹配的正在表达式部分替换为其他值(pattern, repl, string, count=0, flags=0)
sp = re.split(r',| |=', 'zjut ljhmath = 90, ljhpython = 99') #split(pattern, str, maxsplit = 0, flags = 0)根据匹配分割字符串，返回分割字符串组成的列表
print(ma4.group())