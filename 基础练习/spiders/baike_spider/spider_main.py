#! usr/bin/env python3
#-*- coding:utf-8 -*-
from __future__ import absolute_import
import downloader, html_parser, outputer, urlmanager
class SpiderMain(object):
    def __init__(self):
        self.urls = urlmanager.UrlManager()
        self.downloader = downloader.HtmlDonloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)                         #1.添加一个url路径
        while self.urls.has_new_url():                          #2.如果存在一个新的url
            try:
                new_url = self.urls.get_new_url()               #3.获取新的url
                print('craw %d : %s'%(count, new_url))          #打印数量和url
                html_cont = self.downloader.download(new_url)   #4.下载新的url转换为html文档
                new_urls, new_data = self.parser.parse(new_url, html_cont) #5.传入新的url和html文档进行解析穿出关联url路径及新的数据消息
                self.urls.add_new_urls(new_urls)                #6.添加新的url路径到url管理器
                self.outputer.collect_data(new_data)            #7.收集新的消息数据
                if count == 50:
                    break

                count += 1
            except:
                print('craw failed')        
        self.outputer.output_html()                             #输出价值数据

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)