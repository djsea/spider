'''
使用urllib.request请求一个网页内容,病吧内容答应出来
'''

from urllib import request

if __name__ == '__main__':
    url = "http://jobs.zhaopin.com/CC455273028J00023233211.htm"
    # 打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果打印出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))

    html = html.decode()

    print(html)