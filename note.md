# 0 爬虫准备工作
## 参考资料
- python网络数据采集
- 精通python爬虫框架scrapy
- python3网络爬虫
- scrapy官方教程
## 前提知识
- url
- http协议
- web前端、html、css、js
- ajax
- re、xpath
- xml

## 1、爬虫的简介
- 爬虫定义：网络爬虫
- 两大特征
    - 能按照作者要求下载数据或者内容
    - 能自动在网络上流窜
    
- 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
    
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- Python网络包简介
    - python2.x：urllib，urllib2，httplib，httplib2，requests
    - python3.x：urllib，urllib3，httplib2，requests
    - python2.x：urllib和urllib2配合使用，或requests
    - python3.x：urllib，requests
    
# 2.urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:包含urllib.request产生的常见的错误,使用try扑捉
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
    - 案例v1
    
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式,但是,不一定准
    - 需要安装chardet:source activate spider
                      conda install chardet
    - 案例v2
    
- urlopen的返回对象
    - 案例v3
    - geturl:返回请求对象的url
    - info:请求反馈对象的meta信息
    - getcode:返回的http code

- request.data的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递消息
            - 参数为dict,然后使用parse编码
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息,需要利用到data参数
            - 使用post,意味着http的请求头可能需要更改
                - content-type:application/x-www.form-urlencode
                - content-length:数据长度
                - 简而言之,一旦更改请求方法,请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例 v4/v5