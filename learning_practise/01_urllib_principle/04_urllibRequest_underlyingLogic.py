import urllib.request


def handler_openner():
    # 系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能
    # 安全 套接层 ssl第三方的CA数字证书
    # http80端口# 和https443
    # urlopen为什么可以请求数据 handler处理器
    # 自己的oppener请求数据

    # urllib.request.urlopen()
    url = "https://blog.csdn.net/m0_37499059/article/details/79003731"

    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的oppener
    opener = urllib.request.build_opener(handler)
    # 用自己创建的opener调用open方法请求数据
    response = opener.open(url)
    # data = response.read()
    data = response.read().decode("utf-8")

    with open("02header.html", "w")as f:
        f.write(data)


handler_openner()
