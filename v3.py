'''
利用request下载页面
自动检测页面编码
'''


import urllib
import urllib.request
import chardet
# from urllib import request



if __name__ == '__main__':


    url = 'http://stock.eastmoney.com/news/1406,20180706901952913.html'

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    html = rsp.read()
