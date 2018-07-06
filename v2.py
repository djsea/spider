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

    html = rsp.read()

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding", "utf-8"))

    # print(html)