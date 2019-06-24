import urllib.request


def create_proxy_handler():
    url = "https://blog.csdn.net/m0_37499059/article/details/79003731"

    # 添加代理
    proxy = {
        # 免费的写法
        "http": ""
        # "http":"120.77.249.46:8080"
        # 付费的代理
        # "http":"xiaoming":123@115.

    }
    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建自己opener
    opener = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    response = opener.open(url)
    data = response.read().decode("utf-8")

    with open("03header.html", "w")as f:
        f.write(data)


create_proxy_handler()
