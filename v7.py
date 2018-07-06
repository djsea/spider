'''
URLError的使用
'''
# import urllib
from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    try:

        req = request.Request(url)
        print("req=",type(req))

        rsp = request.urlopen(req)
        print("rsp=",type(rsp))
        html = rsp.read().decode()
        print("html=",type(html))
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)
        print(type(e))