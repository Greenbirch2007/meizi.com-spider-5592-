#! -*- coding:utf-8 -*-

from multiprocessing import Pool
import re
import requests
import time
import os
import urllib.request



def get_one_page(url):
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection': 'Keep-Alive',
               'Host': 'zhannei.baidu.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return(response.text)

    else:
        return None


def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
        print('完成！')
    print('%.2f%%' % per)



# def parse_one_page(html):
#     patt = re.compile('<img alt=.*?src="(.*?)" /><br />',re.S)
#     items = re.findall(patt,html)
#     print(items)


        # urllib.request.urlretrieve(item,'/media/karson/交易室/pictures/%s' % item[-10:], Schedule)


url = "http://www.meizitu.com/a/5558.html"
html = get_one_page(url)
print(html)


爬去ip，制作Ip池t in

#  需要破封ip



