#! usr/bin/env python3
#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re

html_doc = """<div class="tool-iseasy r"><strong>难度：</strong>
<a href="/course/list?c=python" class="sort-item active">全部</a>
<a href="/course/list?c=python&is_easy=1" class="sort-item">入门</a>
<a href="/course/list?c=python&is_easy=2" class="sort-item">初级</a>
<a href="/course/list?c=python&is_easy=3" class="sort-item">中级</a>
<a href="/course/list?c=python&is_easy=4" class="sort-item">高级</a>
</div>"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8') #第一个为html文档字符串， 第二个为html解析器， 第三个为html的文档编码
links = soup.find_all('a')
# for link in links:
#     print(link.name, link['href'], link.get_text())
link_node = soup.find('a', href='/course/list?c=python') #第一个是html标签， 第二个是标签内容
#print(link_node.name, link_node['href'], link_node.get_text())

link_node = soup.find('a', href=re.compile(r'3'))
#print(link_node.name, link_node['href'], link_node.get_text())

p_node = soup.find('div', class_=re.compile(r'tool'))
print(p_node.name, p_node.get_text())